# app/schemas/transcript.py
from typing import List
from pydantic import BaseModel, Field
from app.schemas.task import TaskRead


class TranscriptInput(BaseModel):
    """Incoming transcript submission payload."""
    transcript: str = Field(..., description="Raw transcript text to process.")


class TranscriptResponse(BaseModel):
    """Response after transcript is processed into tasks."""
    tasks: List[TaskRead] = Field(
        ...,
        description="Tasks extracted and saved from the transcript."
    )
