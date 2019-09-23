"""
Define the REST verbs relative to the users
"""
from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import UserRepository
from util import parse_params

class UserResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/user/GET.yml")
    def get(last_name, first_name):
        """ Return a user of key information based on the first and last name """
        # users = UserRepository.get()
        users = UserRepository.get(last_name=last_name, first_name=first_name)
        # return [user.json for user in users]
        return jsonify({"user": users.json})


    @staticmethod
    # @parse_params(
    #     Argument("age", location="json", required=True, help="The age of the user.")
    # )
    @swag_from("../swagger/user/POST.yml")
    def post(last_name, first_name, age=None):
        """ Adds a new user """
        user = UserRepository.create(
            last_name=last_name, first_name=first_name, age=age)
        return jsonify({"user": user.json})


    @staticmethod
    @parse_params(
        Argument("age", location="json", required=True, help="The age of the user.123")
    )
    @swag_from("../swagger/user/PUT.yml")
    def put(last_name, first_name, age):
        """ Update an user based on the sent information """
        user = UserRepository.update(
            last_name=last_name, first_name=first_name, age=age)
        return jsonify({"user": user.json})