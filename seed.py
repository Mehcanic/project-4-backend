from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app import app, db
from models.user_model import UserModel
from models.task_model import TaskModel
from models.list_of_tasks_model import ListOfTasksModel

with app.app_context():
    try:
        print("Creating tables...")
        db.drop_all()
        db.create_all()
        print("Tables created!")

        user = UserModel(
            username="lukasz", email="lukasz@lukasz.com", password="password"
        )
        user.save()

        list_of_tasks = ListOfTasksModel(name="To do list", user_id=user.id, user=user)
        list_of_tasks.save()

        date = datetime.strptime("2021-05-01", "%Y-%m-%d")
        time = datetime.strptime("12:00", "%H:%M")
        task = TaskModel(
            name="To do something",
            description="To do something - twice a day",
            status="Active",
            category="Work",
            date=date,
            time=time,
            user_id=user.id,
            list_of_tasks_id=list_of_tasks.id,
        )
        task.save()

        print("Database seeded!")
    except (SQLAlchemyError, IntegrityError) as e:
        print("Error seeding database")
        print(e)
