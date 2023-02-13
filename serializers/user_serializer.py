from marshmallow import fields

from app import ma
from models.user_model import UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    tasks = fields.Nested("TaskSchema", many=True, exclude=("user",))
    list_of_tasks = fields.Nested("LabelSchema", many=True, exclude=("user",))

    class Meta:
        model = UserModel
        load_instance = True
        include_relationships = True
        include_fk = True
