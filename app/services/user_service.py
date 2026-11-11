from sqlalchemy import select

from app.extensions import db
from app.models.user import User


def create_user(username: str, email: str, password_hash: str):
    user = User(username=username, email=email, password_hash=password_hash) # Create an object of our model

    db.session.add(user) # The object is added to the session
    db.session.commit()
    return user


def get_user_by_id(user_id: int):
    statement = select(User).where(User.id == user_id)
    return db.session.execute(statement).scalar_one_or_none()


def get_all_users():
    statement = select(User).order_by(User.id)
    return db.session.execute(statement).scalars().all()


def update_user(user_id: int, username: str = None, email: str = None):
    user = get_user_by_id(user_id)

    if user is None:
        return None

    if username is not None:
        user.username = username

    if email is not None:
        user.email = email

    db.session.commit()
    return user


def delete_user(user_id: int):
    user = get_user_by_id(user_id)

    if user is None:
        return False

    db.session.delete(user)
    db.session.commit()
    return True
