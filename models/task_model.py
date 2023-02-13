from app import db

from models.base import BaseModel

# from models.list_of_tasks_model import ListOfTasksModel
# from models.user_model import UserModel


class TaskModel(db.Model, BaseModel):
    __tablename__ = "tasks"
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    list_of_tasks_id = db.Column(
        db.Integer, db.ForeignKey("list_of_tasks.id"), nullable=False
    )

    user = db.relationship("UserModel", back_populates="task")
    lists_of_tasks = db.relationship("ListOfTasksModel", back_populates="task")

    def __repr__(self):
        return f"<Task {self.name}>"
