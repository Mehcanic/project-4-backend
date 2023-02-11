from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config.environment import db_URI

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

ma = Marshmallow(app)

from controllers import users_controllers


app.register_blueprint(users_controllers.router, url_prefix="/api")
