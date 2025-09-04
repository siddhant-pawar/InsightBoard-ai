# app/utils/text.py
import re
import unicodedata

def sanitize_transcript(transcript: str) -> str:
    """
    Clean and normalize transcript text for LLM / NLP ingestion.

    - Normalize Unicode (NFC)
    - Normalize line endings to Unix style
    - Remove control characters (keep \t and \n)
    - Remove/strip Markdown markers more intelligently:
      * remove heading markers at line start
      * remove list markers at line start (-, *, +)
      * remove blockquote '>' at line start
      * remove code fences (```...```) but keep fenced content
      * unwrap inline code/backticks, bold, italics (keep inner text)
    - Collapse multiple spaces/tabs into single space
    - Collapse 3+ newlines into max 2
    - Strip leading/trailing whitespace
    """

    if not transcript:
        return ""

    # Normalize unicode (combine accents, etc.)
    text = unicodedata.normalize("NFC", transcript)

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove control characters except tab and newline
    text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]+', ' ', text)

    # --- Markdown-aware cleanup ---

    # Remove code fences but keep the inner content
    text = re.sub(r'```(?:[\w+-]*\n)?(.*?)```', r'\1', text, flags=re.S)

    # Unwrap inline code: `code` -> code
    text = re.sub(r'`([^`]*)`', r'\1', text)

    # Unwrap bold and italic markers while preserving the inner text
    text = re.sub(r'(\*\*|__)(.*?)\1', r'\2', text, flags=re.S)
    text = re.sub(r'(\*|_)(.*?)\1', r'\2', text, flags=re.S)

    # Remove heading markers at start of line: "## Title" -> "Title"
    text = re.sub(r'(?m)^\s{0,3}#{1,6}\s*', '', text)

    # Remove leading list markers at start of line: "- item" or "* item" or "+ item"
    text = re.sub(r'(?m)^\s*[-*+]\s+', '', text)

    # Remove blockquote markers at line start: "> quoted" -> "quoted"
    text = re.sub(r'(?m)^\s{0,3}>\s?', '', text)

    # Remove stray backslashes (optional) but do this after handling code
    text = text.replace('\\', '')

    # Collapse multiple spaces / tabs into one
    text = re.sub(r'[ \t]+', ' ', text)

    # Collapse many blank lines into max two newlines
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Strip leading/trailing whitespace
    return text.strip()
