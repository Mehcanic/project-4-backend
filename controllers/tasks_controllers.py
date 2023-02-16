from http import HTTPStatus
from flask import Blueprint, request
from marshmallow.exceptions import ValidationError

from models.task_model import TaskModel
from serializers.task_serializer import TaskSchema

task_schema = TaskSchema()

router = Blueprint("tasks_controllers", __name__)


@router.route("/users/tasks", methods=["GET"])
def get_all_tasks():
    tasks = TaskModel.query.all()
    return task_schema.jsonify(tasks, many=True), HTTPStatus.OK


@router.route("/users/tasks/<int:task_id>", methods=["GET"])
def get_single_task(task_id):
    task = TaskModel.query.get(task_id)
    return task_schema.jsonify(task), HTTPStatus.OK


@router.route("/users/tasks", methods=["POST"])
def create_task():
    task_dictionary = request.json
    existing_task = TaskModel.query.filter_by(name=task_dictionary['name']).first()

    if existing_task:
        return {"message": "Task already exists"}, HTTPStatus.BAD_REQUEST

    try:
        task = task_schema.load(task_dictionary)
        task.save()
    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong when creating the task"
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    return task_schema.jsonify(task), HTTPStatus.CREATED


@router.route("/users/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task_dictionary = request.json
    task = TaskModel.query.get(task_id)
    if not task:
        return {"message": "Task not found"}, HTTPStatus.NOT_FOUND

    try:
        task = task_schema.load(task_dictionary, instance=task, partial=True)
        task.save()
    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong when updating the task"
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    return task_schema.jsonify(task), HTTPStatus.OK


@router.route("/users/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = TaskModel.query.get(task_id)

    if not task:
        return {"message": "Task not found"}, HTTPStatus.NOT_FOUND
    task.delete()
    return {"message": "Task deleted seccesfully"}, HTTPStatus.NO_CONTENT