from sqlalchemy import select

from app.extensions import db
from app.models.task import Task, TaskStatus, TaskPriority


def create_task(
    title: str,
    description: str | None,
    project_id: int,
    assignee_id: int | None = None,
    priority: TaskPriority = TaskPriority.MEDIUM
):
    task = Task(
        title=title,
        description=description,
        project_id=project_id,
        assignee_id=assignee_id,
        priority=priority
    )

    db.session.add(task)
    db.session.commit()

    return task


def get_task_by_id(task_id: int):
    statement = select(Task).where(Task.id == task_id)

    return db.session.execute(statement).scalar_one_or_none()


def get_project_tasks(project_id: int):
    statement = (
        select(Task)
        .where(Task.project_id == project_id)
        .order_by(Task.id)
    )

    return db.session.execute(statement).scalars().all()


def update_task_status(task_id: int, status: TaskStatus):
    task = get_task_by_id(task_id)

    if task is None:
        return None

    task.status = status
    db.session.commit()

    return task


def delete_task(task_id: int):
    task = get_task_by_id(task_id)

    if task is None:
        return False

    db.session.delete(task)
    db.session.commit()

    return True
