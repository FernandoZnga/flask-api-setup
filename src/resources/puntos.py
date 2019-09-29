"""
Define las acciones REST relacionados a los puntos
"""
from flasgger import swag_from
from flask.json import jsonify
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import PuntosRepository
from util import parse_params

class PuntosResource(Resource):
    """ Acciones relacionado a los puntos """

    @staticmethod
    def get():
        """ Retorna un cliente con sus respectivos puntos """
        pass

    @staticmethod
    def post():
        """ Asignar puntos a un cliente """
        pass

    @staticmethod
    def put():
        """ Actualiza el saldo de puntos """
        pass

    @staticmethod
    def delete():
        """ Elimina la cuenta de puntos """
        pass