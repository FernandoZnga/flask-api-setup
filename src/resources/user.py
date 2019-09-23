"""
Define the REST verbs relative to the users
"""
from flask_restful import Resource
from repositories import UserRepository

class UserResource(Resource):
    """ Verbs relative to the users """

    def get(self):
        """ Return a list of key information about users """
        user_repository = UserRepository()
        users = user_repository.get()
        return [user.json for user in users]