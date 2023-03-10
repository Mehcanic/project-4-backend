from app import ma
from models.task_model import TaskModel

class TaskSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = TaskModel
        load_instance = True
        include_fk = True