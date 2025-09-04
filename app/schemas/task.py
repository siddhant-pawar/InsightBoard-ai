# app/schemas/task.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class TaskBase(BaseModel):
    text: str
    priority: str = "medium"
    tags: List[str] = []
    status: str = "pending"


class TaskCreate(TaskBase):
    source_id: Optional[str] = None


class TaskUpdate(BaseModel):
    text: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None


class TaskRead(TaskBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class TaskFilterInput(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None
    keyword: Optional[str] = None
    tags: Optional[List[str]] = None
    sort_by: str = "created_at"
    order: str = "desc"