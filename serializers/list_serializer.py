from app import ma
from models.list_of_tasks_model import ListOfTasksModel


class ListSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ListOfTasksModel
        load_instance = True
        include_fk = True
