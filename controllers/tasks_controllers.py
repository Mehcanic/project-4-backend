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
    existing_task = TaskModel.query.filter_by(name=task_dictionary["name"]).first()

    if existing_task:
        return {"message": "Task already exists"}, HTTPStatus.BAD_REQUEST

    try:
        task = task_schema.load(task_dictionary)
        task.save()
    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong when creating the task",
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
            "message": "Something went wrong when updating the task",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    return task_schema.jsonify(task), HTTPStatus.OK


@router.route("/users/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = TaskModel.query.get(task_id)

    if not task:
        return {"message": "Task not found"}, HTTPStatus.NOT_FOUND
    task.delete()
    return {"message": "Task deleted seccesfully"}, HTTPStatus.NO_CONTENT


# Create funtion to filter for tasks based on description or name
@router.route("/users/tasks/<string:params>", methods=["GET"])
def filter_tasks_by_params():
    try:
        name = request.args.get("name")
        description = request.args.get("description")
        category = request.args.get("category")
        status = request.args.get("status")
        date = request.args.get("date")
        time = request.args.get("time")

        query = TaskModel.query

        if name:
            query = query.filter(TaskModel.name.ilike(f"%{name}%"))
        if description:
            query = query.filter(TaskModel.description.ilike(f"%{description}%"))
        if category:
            query = query.filter(TaskModel.category.ilike(f"%{category}%"))
        if status:
            query = query.filter(TaskModel.status.ilike(f"%{status}%"))
        if date:
            query = query.filter(TaskModel.date.ilike(f"{date}%"))
        if time:
            query = query.filter(TaskModel.time.ilike(f"{time}%"))

        tasks = query.all()
    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong when filtering the tasks",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    return task_schema.jsonify(tasks, many=True), HTTPStatus.OK

