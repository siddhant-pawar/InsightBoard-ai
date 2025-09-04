# app/api/tasks.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.schemas.task import TaskRead, TaskUpdate
from app.schemas.task_filter import TaskFilterInput
from app.services.task_service import list_tasks, update_task, delete_task, filter_tasks

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


@router.get("/", response_model=list[TaskRead])
async def get_tasks(db: AsyncSession = Depends(get_db)):
    """Fetch all tasks."""
    return await list_tasks(db)


@router.patch("/{task_id}", response_model=TaskRead)
async def patch_task(
    task_id: str, patch: TaskUpdate, db: AsyncSession = Depends(get_db)
):
    """Update a task by ID."""
    updated = await update_task(db, task_id, patch)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return updated


@router.delete("/{task_id}")
async def remove_task(task_id: str, db: AsyncSession = Depends(get_db)):
    """Delete a task by ID."""
    deleted = await delete_task(db, task_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return {"status": "deleted"}


@router.post("/filter", response_model=list[TaskRead])
async def get_filtered_tasks(
    filters: TaskFilterInput, db: AsyncSession = Depends(get_db)
):

    return await filter_tasks(
        db,
        status=filters.status,
        priority=filters.priority,
        keyword=filters.keyword,
        tags=filters.tags,
        sort_by=filters.sort_by,
        order=filters.order,
    )
