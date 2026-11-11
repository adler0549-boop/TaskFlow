from datetime import datetime, timezone

from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extensions import db

import enum


class TaskStatus(enum.Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskPriority(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Task(db.Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        db.String(150),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        db.Text,
        nullable=True
    )

    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus),
        default=TaskStatus.TODO,
        nullable=False
    )

    priority: Mapped[TaskPriority] = mapped_column(
        Enum(TaskPriority),
        default=TaskPriority.MEDIUM,
        nullable=False
    )

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id"),
        nullable=False
    )

    assignee_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    project: Mapped["Project"] = relationship(
        back_populates="tasks"
    )

    assignee: Mapped["User | None"] = relationship(
        back_populates="assigned_tasks"
    )

    def __repr__(self):
        return f"<Task {self.title}>"
