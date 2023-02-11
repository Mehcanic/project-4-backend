from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from app import app, db
from models.user_model import UserModel

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

        print("Database seeded!")
    except (SQLAlchemyError, IntegrityError) as e:
        print("Error seeding database")
        print(e)
