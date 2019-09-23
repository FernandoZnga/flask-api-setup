"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import UserResource


USER_BLUEPRINT = Blueprint("user", __name__)
Api(USER_BLUEPRINT).add_resource(UserResource, "/user/<string:last_name>/<string:first_name>")

ADD_BLUEPRINT = Blueprint("add", __name__)
Api(ADD_BLUEPRINT).add_resource(UserResource, "/add/<string:last_name>/<string:first_name>/<int:age>")

UPDATE_BLUEPRINT = Blueprint("update", __name__)
Api(UPDATE_BLUEPRINT).add_resource(UserResource, "/update/<string:last_name>/<string:first_name>")