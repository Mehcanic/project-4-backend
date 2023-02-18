from http import HTTPStatus
from flask import Blueprint, request

from marshmallow.exceptions import ValidationError

from models.list_of_tasks_model import ListOfTasksModel

from serializers.list_serializer import ListSchema

list_of_tasks_schema = ListSchema()

router = Blueprint("list_of_tasks_controllers", __name__)


@router.route("/users/lists", methods=["GET"])
def get_all_lists_of_tasks():
    lists_of_tasks = ListOfTasksModel.query.all()
    return list_of_tasks_schema.jsonify(lists_of_tasks, many=True), HTTPStatus.OK


@router.route("/users/lists/<int:list_of_tasks_id>", methods=["GET"])
def get_single_list_of_tasks(list_of_tasks_id):
    list_of_tasks = ListOfTasksModel.query.get(list_of_tasks_id)
    return list_of_tasks_schema.jsonify(list_of_tasks), HTTPStatus.OK


@router.route("/users/lists", methods=["POST"])
def create_list_of_tasks():
    list_of_tasks_dictionary = request.json
    existing_list_of_tasks = ListOfTasksModel.query.filter_by(
        name=list_of_tasks_dictionary["name"]
    ).first()

    if existing_list_of_tasks:
        return {"message": "List of tasks already exists"}, HTTPStatus.BAD_REQUEST

    try:
        list_of_tasks = list_of_tasks_schema.load(list_of_tasks_dictionary)
        list_of_tasks.save()
    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong when creating the list of tasks",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    return list_of_tasks_schema.jsonify(list_of_tasks), HTTPStatus.CREATED


@router.route("/users/lists/<int:list_of_tasks_id>", methods=["PUT"])
def update_list_of_tasks(list_of_tasks_id):
    list_of_tasks_dictionary = request.json
    list_of_tasks = ListOfTasksModel.query.get(list_of_tasks_id)
    if not list_of_tasks:
        return {"message": "List of tasks not found"}, HTTPStatus.NOT_FOUND

    try:
        list_of_tasks = list_of_tasks_schema.load(
            list_of_tasks_dictionary, instance=list_of_tasks, partial=True
        )
        list_of_tasks.save()
    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong when updating the list of tasks",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    return list_of_tasks_schema.jsonify(list_of_tasks), HTTPStatus.OK


@router.route("/users/lists/<int:list_of_tasks_id>", methods=["DELETE"])
def delete_list_of_tasks(list_of_tasks_id):
    list_of_tasks = ListOfTasksModel.query.get(list_of_tasks_id)

    if not list_of_tasks:
        return {"message": "List of tasks not found"}, HTTPStatus.NOT_FOUND
    list_of_tasks.delete()
    return {"message": "List deleted seccesfully"}, HTTPStatus.NO_CONTENT
