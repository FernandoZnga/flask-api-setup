"""
Define the REST verbs relative to the users
"""
from flasgger import swag_from
from flask.json import jsonify
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import UserRepository
from util import parse_params

class UserResource(Resource):
    """ Verbs relative to the users """


    @staticmethod
    # @swag_from("../swagger/user/GET.yml")
    def get():
        """ Return a user of key information based on the first and last name """
        users = UserRepository.get()
        # users = UserRepository.get(last_name=last_name, first_name=first_name)
        return [user.json for user in users]
        # return jsonify({"user": users.json})


    @staticmethod
    # @swag_from("../swagger/user/POST.yml")
    def post():
        """ Adds a new user """
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No imput data provided"},400
        
        last_name = json_data.get("last_name")
        first_name = json_data.get("first_name")
        age = json_data.get("age")

        user = UserRepository.create(last_name, first_name, age)
        return jsonify({"create_user": user.json})


    @staticmethod
    # @swag_from("../swagger/user/PUT.yml")
    def put():
        """ Update an user based on the sent information """
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No imput data provided"},400
        
        last_name = json_data.get("last_name")
        first_name = json_data.get("first_name")
        age = json_data.get("age")

        user = UserRepository.update(last_name, first_name, age)
        return jsonify({"update_user": user.json})


    @staticmethod
    # @swag_from("../swagger/user/PUT.yml")
    def delete():
        """ Delete an user based on the sent information """
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No imput data provided"},400
        
        last_name = json_data.get("last_name")
        first_name = json_data.get("first_name")
        
        search_user = UserRepository.get_one(last_name=last_name, first_name=first_name)
        if search_user is None:
            pass
        else:
            user = UserRepository.delete(last_name, first_name)
            return jsonify({"delete_user": user.json})