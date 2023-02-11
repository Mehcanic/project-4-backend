from app import db

from models.base import BaseModel


class UserModel(db.Model, BaseModel):
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
