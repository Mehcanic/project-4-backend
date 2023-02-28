from app import db

from models.base import BaseModel

# from models.list_of_tasks_model import ListOfTasksModel
# from models.user_model import UserModel


class TaskModel(db.Model, BaseModel):
    __tablename__ = "tasks"
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    status = db.Column(db.String, nullable=True)
    category = db.Column(db.String, nullable=True)
    date = db.Column(db.String, nullable=True)
    time = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    list_of_tasks_id = db.Column(
        db.Integer, db.ForeignKey("list_of_tasks.id"), nullable=True
    )

    user = db.relationship("UserModel", back_populates="task")
    lists_of_tasks = db.relationship("ListOfTasksModel", back_populates="task")

    def __repr__(self):
        return f"<Task {self.name}>"
