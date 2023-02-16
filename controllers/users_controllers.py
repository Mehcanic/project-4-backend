from http import HTTPStatus
from flask import Blueprint, request
from marshmallow.exceptions import ValidationError

from models.user_model import UserModel
from serializers.user_serializer import UserSchema

user_schema = UserSchema()

router = Blueprint("users_controllers", __name__)


@router.route("/users", methods=["GET"])
def get_all_users():
    users = UserModel.query.all()
    return user_schema.jsonify(users, many=True), HTTPStatus.OK


@router.route("/users/<int:user_id>", methods=["GET"])
def get_single_user(user_id):
    user = UserModel.query.get(user_id)
    return user_schema.jsonify(user), HTTPStatus.OK


@router.route("/users", methods=["POST"])
def create_user():
    user_dictionary = request.json
    existing_user = UserModel.query.filter_by(email=user_dictionary["email"]).first()

    if existing_user:
        return {"message": "User already exists"}, HTTPStatus.BAD_REQUEST

    try:
        user = user_schema.load(user_dictionary)
        user.save()
    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong when creating the user",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    return user_schema.jsonify(user), HTTPStatus.CREATED


# @router.route("/users", methods=["POST"])
# def login():
#     user_dictionary = request.json
#     user = UserModel.query.filter_by(email=user_dictionary['email']).first()

#     if not user:
#         return {
#             "message": "Incorrect email or password"
#         }, HTTPStatus.UNAUTHORIZED

#     token = user.generate_token()

#     return {"token": token, "message": "Successfully logged in"}, HTTPStatus.OK


@router.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user_dictionary = request.json
    user = UserModel.query.get(user_id)

    if not user:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND

    try:
        user = user_schema.load(user_dictionary, instance=user, partial=True)
        user.save()
    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong when updating the user",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    return user_schema.jsonify(user), HTTPStatus.OK


@router.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = UserModel.query.get(user_id)

    if not user:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND
    user.delete()
    return {"message": "User deleted successfully"}, HTTPStatus.OK