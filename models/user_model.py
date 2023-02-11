# setup model for the user table

from app import db, app
from flask import flask, request, jsonify


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name