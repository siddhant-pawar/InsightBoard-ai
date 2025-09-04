# app/api/transcripts.py
import logging
import asyncio
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.services import ai_service
from app.services.task_service import create_tasks
from app.utils.text import sanitize_transcript
from app.schemas.transcript import TranscriptInput, TranscriptResponse
from app.schemas.task import TaskCreate, TaskRead

router = APIRouter(prefix="/api/transcripts", tags=["transcripts"])


@router.post("/", response_model=TranscriptResponse, status_code=status.HTTP_200_OK)
async def submit_transcript(
    payload: TranscriptInput, db: AsyncSession = Depends(get_db)
):
    """Accepts a raw transcript, extracts actionable tasks, saves them, and returns them."""
    transcript = sanitize_transcript(payload.transcript)

    if not transcript:
        raise HTTPException(status_code=400, detail="Transcript is empty.")

    # --- Extract tasks from AI service ---
    try:
        if asyncio.iscoroutinefunction(ai_service.extract_tasks):
            tasks = await ai_service.extract_tasks(transcript)
        else:
            tasks = await asyncio.to_thread(ai_service.extract_tasks, transcript)
    except Exception:
        logging.exception("Error during extract_tasks")
        raise HTTPException(
            status_code=500, detail="Failed to extract tasks from transcript."
        )

    if not tasks:
        return {"tasks": []}

    # --- Persist extracted tasks ---
    try:
        created: list[TaskRead] = await create_tasks(db, tasks)
    except Exception:
        logging.exception("Error during create_tasks")
        raise HTTPException(
            status_code=500, detail="Failed to save tasks to database."
        )

    return {"tasks": created}
