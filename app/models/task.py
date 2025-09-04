# app/models/task.py
import uuid
import enum
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import ARRAY

Base = declarative_base()


class StatusEnum(str, enum.Enum):
    pending = "pending"
    completed = "completed"


class PriorityEnum(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Task(Base):
    __tablename__ = "tasks"

    id = sa.Column(
        sa.String, primary_key=True, default=lambda: str(uuid.uuid4())
    )
    text = sa.Column(sa.String, nullable=False)

    status = sa.Column(
        sa.Enum(StatusEnum, name="statusenum"),
        nullable=False,
        server_default="pending",
    )
    priority = sa.Column(
        sa.Enum(PriorityEnum, name="priorityenum"),
        nullable=False,
        server_default="medium",
    )

    # ✅ Postgres ARRAY type, supports .contains() and .overlap()
    tags = sa.Column(ARRAY(sa.String), server_default="{}")

    created_at = sa.Column(sa.DateTime, server_default=sa.text("now()"))
    updated_at = sa.Column(
        sa.DateTime,
        server_default=sa.text("now()"),
        onupdate=sa.text("now()"),
    )

    source_id = sa.Column(sa.String, unique=True, nullable=True)
