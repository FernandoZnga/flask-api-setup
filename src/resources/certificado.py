"""
Define las acciones REST relacionados a los certificados
"""
from flasgger import swag_from
from flask.json import jsonify
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import CertificadoRepository
from util import parse_params

class CertificadoResource(Resource):
    """ Acciones relacionado a los certificados """

    @staticmethod
    def get():
        """ Retorna un certificado disponible para asignar """
        pass

    @staticmethod
    def post():
        """ A un certificado disponible, se le asigna el saldo y el cliente"""
        pass

    @staticmethod
    def put():
        """ Actualiza el saldo de un certificado """
        pass

    @staticmethod
    def delete():
        """ Elimina un certificado previamente asignado """
        pass