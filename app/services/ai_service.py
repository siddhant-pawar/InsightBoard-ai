# app/services/ai_service.py
import os
import json
import uuid
import logging
import asyncio
from typing import List

from openai import AsyncOpenAI, APITimeoutError, APIError
from app.schemas.task import TaskCreate

# make client a module-level singleton
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def extract_tasks(transcript: str, *, max_retries: int = 3, retry_base_delay: float = 1.0) -> List[TaskCreate]:
    """
    Extract actionable tasks from `transcript` using the OpenAI Async client.
    Returns a list of TaskCreate Pydantic models.

    Defensive: retries transient errors, tolerates different response shapes, normalizes keys.
    """

    # Strict instruction: model must output only a JSON array (no extra commentary)
    system = (
        "You are a JSON-only extractor. Given a transcript, return EXACTLY a JSON array (and nothing else) "
        "where each element is an object with keys: id (string), text (string), priority (one of: low, medium, high), tags (array of strings). "
        "If a field is unknown, set it to null, empty string, or an empty array. Do NOT output explanations or markdown."
    )

    # Provide a short example to reduce ambiguity
    example = (
        "Example output:\n"
        '[\n'
        '  { "id": "1", "text": "Fix payment gateway race condition", "priority": "high", "tags": ["payments","backend"] },\n'
        '  { "id": "2", "text": "Run full regression tests over weekend", "priority": "high", "tags": ["qa","regression"] }\n'
        "]"
    )

    user = f"{example}\n\nTranscript:\n'''{transcript}'''"

    for attempt in range(1, max_retries + 1):
        try:
            resp = await client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                temperature=0.0,
                max_tokens=800,
            )

            # --- robust extraction of the "content" ---
            content = None

            # Different SDKs/response shapes exist; handle defensively
            if hasattr(resp, "choices") and len(resp.choices) > 0:
                choice = resp.choices[0]
                # Newer SDK shapes may have `.message.content`, older may have `.text` or `.message["content"]`
                if getattr(choice, "message", None) is not None:
                    content = getattr(choice.message, "content", None)
                    if content is None and isinstance(choice.message, dict):
                        content = choice.message.get("content")
                elif hasattr(choice, "text"):
                    content = choice.text
                elif hasattr(choice, "content"):
                    content = choice.content
                else:
                    # fallback to string representation
                    content = str(choice)
            else:
                # fallback if SDK puts text elsewhere
                content = getattr(resp, "content", None) or str(resp)

            if content is None:
                raise RuntimeError("OpenAI response contains no content.")

            # If it's already a dict/list, keep it. If it's a string, parse JSON out of it.
            parsed = None
            if isinstance(content, (dict, list)):
                parsed = content
            else:
                text = str(content).strip()
                # The model might sometimes prepend explanation; try to find the first JSON bracket
                first_brace = min(
                    (idx for idx in (text.find("["), text.find("{")) if idx != -1),
                    default=0
                )
                if first_brace > 0:
                    text = text[first_brace:]
                parsed = json.loads(text)  # may raise

            # Normalize parsed into tasks list:
            if isinstance(parsed, list):
                tasks_raw = parsed
            elif isinstance(parsed, dict) and "tasks" in parsed and isinstance(parsed["tasks"], list):
                tasks_raw = parsed["tasks"]
            else:
                # If the model returned a dict of items, try to coerce its values to a list
                if isinstance(parsed, dict):
                    # sometimes model returns {"1": {...}, "2": {...}}
                    possible = []
                    for v in parsed.values():
                        if isinstance(v, dict):
                            possible.append(v)
                    tasks_raw = possible
                else:
                    tasks_raw = []

            result: List[TaskCreate] = []
            for raw in tasks_raw:
                if not isinstance(raw, dict):
                    logging.warning("Skipping non-dict task element: %r", raw)
                    continue

                # flexible key mapping
                text_val = raw.get("text") or raw.get("title") or raw.get("task") or ""
                id_val = raw.get("id") or raw.get("task_id") or str(uuid.uuid4())
                pr = (raw.get("priority") or "").lower() if raw.get("priority") else ""
                if pr not in ("low", "medium", "high"):
                    pr = "medium"  # default fallback
                tags_val = raw.get("tags") or raw.get("labels") or []
                if not isinstance(tags_val, list):
                    # if model returns comma-joined tags string, split it
                    if isinstance(tags_val, str):
                        tags_val = [t.strip() for t in tags_val.split(",") if t.strip()]
                    else:
                        tags_val = []

                # Build pydantic model (this will validate types too)
                try:
                    task_obj = TaskCreate(id=id_val, text=text_val, priority=pr, tags=tags_val)
                    result.append(task_obj)
                except Exception as e:
                    logging.exception("Failed to construct TaskCreate for raw=%r: %s", raw, e)
                    # skip invalid entries

            return result

        except (APITimeoutError, asyncio.TimeoutError) as e:
            logging.warning("OpenAI timeout (attempt %d/%d): %s", attempt, max_retries, e)
            if attempt == max_retries:
                raise RuntimeError("OpenAI request timed out")
        except APIError as e:
            logging.warning("OpenAI API error (attempt %d/%d): %s", attempt, max_retries, e)
            if attempt == max_retries:
                raise RuntimeError(f"OpenAI API error: {str(e)}")
        except json.JSONDecodeError as e:
            logging.exception("JSON decode error when parsing OpenAI response (attempt %d/%d): %s", attempt, max_retries, e)
            if attempt == max_retries:
                raise RuntimeError(f"Failed to parse OpenAI response as JSON: {str(e)}")
        except Exception as e:
            logging.exception("Unexpected error in extract_tasks (attempt %d/%d): %s", attempt, max_retries, e)
            # fail fast for unexpected exceptions
            raise RuntimeError(f"Unexpected error extracting tasks: {e}")

        # exponential backoff before retrying
        await asyncio.sleep(retry_base_delay * (2 ** (attempt - 1)))

    # should not reach here
    return []
