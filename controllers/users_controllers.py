from http import HTTPStatus
from flask import Blueprint

from models.user_model import UserModel
from serializers.user_serializer import UserSchema

user_schema = UserSchema()


router = Blueprint("users_controllers", __name__)


@router.route("/users", methods=["GET"])
def get_all_users():
    users = UserModel.query.all()
    return user_schema.jsonify(users, many=True), HTTPStatus.OK
