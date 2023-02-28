from app import db

from models.base import BaseModel

from models.list_of_tasks_model import ListOfTasksModel
from models.task_model import TaskModel


class UserModel(db.Model, BaseModel):
    __tablename__ = "users"
    username = db.Column(db.String, unique=True, nullable=True)
    email = db.Column(db.Text, unique=True, nullable=True)
    password = db.Column(db.String, nullable=True)

    task = db.relationship("TaskModel", back_populates="user")
    lists_of_tasks = db.relationship("ListOfTasksModel", back_populates="user")

    def __repr__(self):
        return f"<User {self.username}>"
