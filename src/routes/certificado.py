"""
Define los blueprints para los certificados
"""
from flask import Blueprint
from flask_restful import Api

from resources import CertificadoResource

CERTIFICADO_BLUEPRINT = Blueprint('certificado',__name__)

## Routes ##

Api(CERTIFICADO_BLUEPRINT).add_resource(CertificadoResource, '/certificado')