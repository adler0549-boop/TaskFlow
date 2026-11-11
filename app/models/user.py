from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db


class User(db.Model):
    __tablename__ = "users"

    # unique=True - prohibits repeating values
    # nullable=False - prohibits empty values
    id: Mapped[int] = mapped_column(primary_key=True) # ORM attribute data type, mapped_column - table column
    username: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(db.String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(db.String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    projects: Mapped[list["Project"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
    assigned_tasks: Mapped[list["Task"]] = relationship(back_populates="assignee")

    def __repr__(self):
        return f"<User {self.username}>"
