from app import ma
from models.user_model import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = UserModel
        load_instance = True
        include_relationships = True
        include_fk = True