from flask import Flask

from config import Config
from app.extensions import db, migrate, jwt


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app) # Connects SQLAlchemy
    from app.models import User
    migrate.init_app(app, db) # Connects Alembic migrations
    jwt.init_app(app) # Connects JWT

    return app # Save the change to the app object
