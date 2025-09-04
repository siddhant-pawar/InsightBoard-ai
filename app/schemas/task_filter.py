from typing import Optional, List
from pydantic import BaseModel
from app.models.task import StatusEnum, PriorityEnum

class TaskFilterInput(BaseModel):
    status: Optional[StatusEnum] = None
    priority: Optional[PriorityEnum] = None
    keyword: Optional[str] = None
    tags: Optional[List[str]] = None
    sort_by: str = "created_at"
    order: str = "desc"
