""" Defines the User repository """

from models import User


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(last_name, first_name):
        """ Query every user """
        # return User.query.all()
        return User.query.filter_by(last_name=last_name, first_name=first_name).one()

    @staticmethod
    def create(last_name, first_name, age):
        """ Insert a new user """
        user = User(last_name=last_name, first_name=first_name, age=age)
        return user.save()

    @staticmethod
    def update(last_name, first_name, age):
        """ Update a user """
        user = User(last_name=last_name, first_name=first_name, age=age)
        return user.save()