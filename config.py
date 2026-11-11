import os

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///taskflow.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Unnecessary change tracking is disabled
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key") # key for Flask
