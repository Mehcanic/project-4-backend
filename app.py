from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_cors import CORS

from config.environment import db_URI

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

ma = Marshmallow(app)

CORS(app)

from controllers import users_controllers
from controllers import tasks_controllers
from controllers import list_of_tasks_controllers

app.register_blueprint(users_controllers.router, url_prefix="/api")
app.register_blueprint(tasks_controllers.router, url_prefix="/api")
app.register_blueprint(list_of_tasks_controllers.router, url_prefix="/api")
