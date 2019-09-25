""" Defines the User repository """

from models import User


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get():
        """ Query every user """
        return User.query.all()
        # return User.query.filter_by(last_name=last_name, first_name=first_name).one_or_none()

    @staticmethod
    def create(last_name, first_name, age):
        """ Insert a new user """
        user = User(last_name=last_name, first_name=first_name, age=age)
        return user.save()

    @staticmethod
    def update(last_name, first_name, age):
        """ Update a user """
        user = User.query.filter_by(last_name=last_name, first_name=first_name).one_or_none()
        user.age = age
        return user.save()

    @staticmethod
    def delete(last_name, first_name):
        """ Delete a user """
        user = User.query.filter_by(last_name=last_name, first_name=first_name).one_or_none()
        user.delete()
        return user