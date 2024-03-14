import os

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TASKS_MODIFICATIONS=os.getenv("SQLALCHEMY_TASKS_MODIFICATIONS")

db=SQLAlchemy()