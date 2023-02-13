from app import ma

from models.list_of_tasks_model import ListModel

class ListSchema(ma.SLQAlchemyAutoSchema):

    class Meta:
        model = ListModel
        load_instance = True
        include_fk = True