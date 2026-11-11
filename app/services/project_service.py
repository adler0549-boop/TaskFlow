from sqlalchemy import select

from app.extensions import db
from app.models.project import Project


def create_project(title: str, description: str | None, owner_id: int):
    project = Project(title=title,  description=description, owner_id=owner_id)

    db.session.add(project)
    db.session.commit()
    return project


def get_project_by_id(project_id: int):
    statement = select(Project).where(Project.id == project_id)
    return db.session.execute(statement).scalar_one_or_none()


def get_all_projects():
    statement = select(Project).order_by(Project.id)
    return db.session.execute(statement).scalars().all()


def get_user_projects(owner_id: int):
    statement = (select(Project).where(Project.owner_id == owner_id).order_by(Project.id))
    return db.session.execute(statement).scalars().all()


def update_project(project_id: int, title: str | None = None, description: str | None = None):
    project = get_project_by_id(project_id)

    if project is None:
        return None

    if title is not None:
        project.title = title

    if description is not None:
        project.description = description

    db.session.commit()
    return project


def delete_project(project_id: int):
    project = get_project_by_id(project_id)

    if project is None:
        return False

    db.session.delete(project)
    db.session.commit()

    return True
