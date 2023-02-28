from app import db

from models.base import BaseModel

from models.task_model import TaskModel

# from models.user_model import UserModel


class ListOfTasksModel(db.Model, BaseModel):
    __tablename__ = "list_of_tasks"
    name = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    task = db.relationship("TaskModel", back_populates="lists_of_tasks")
    user = db.relationship("UserModel", back_populates="lists_of_tasks")

    def __repr__(self):
        return f"<Label {self.name}>"
