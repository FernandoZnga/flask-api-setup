"""
Define los blueprints para los puntos
"""
from flask import Blueprint
from flask_restful import Api

from resources import PuntosResource

PUNTOS_BLUEPRINT = Blueprint('puntos',__name__)

## Routes ##

Api(PUNTOS_BLUEPRINT).add_resource(PuntosResource, '/puntos')