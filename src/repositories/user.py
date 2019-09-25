""" Defines the User repository """

from models import User


class UserRepository:
    """ The repository for the user model """


    @staticmethod
    def get_one(last_name, first_name):
        """ Query every user """
        # return User.query.all()
        return User.query.filter_by(last_name=last_name, first_name=first_name).one_or_none()

    @staticmethod
    def get():
        """ Query every user """
        return User.query.all()
        # return User.query.filter_by(last_name=last_name, first_name=first_name).one_or_none()

    @staticmethod
    def create(last_name, first_name, age):
        """ Insert a new user """

        search_user_create = UserRepository.get_one(last_name=last_name, first_name=first_name)
        if search_user_create is None:
            user_create = User(last_name=last_name, first_name=first_name, age=age)
            return user_create.save()
        else:
            return search_user_create

    @staticmethod
    def update(last_name, first_name, age):
        """ Update a user """

        search_user_update = UserRepository.get_one(last_name=last_name, first_name=first_name)
        if search_user_update is None:
            user_update = UserRepository.create(last_name, first_name, age)
            return user_update
        else:
            search_user_update.age = age
            return search_user_update.save()

    @staticmethod
    def delete(last_name, first_name):
        """ Delete a user """

        search_user_delete = UserRepository.get_one(last_name=last_name, first_name=first_name)
        if search_user_delete is None:
            return self
        else:
            search_user_delete.delete()
            return search_user_delete