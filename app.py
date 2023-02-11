from controllers import users_controllers
from sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)


app.register_blueprint(users_controllers.router, url_prefix="/api")
