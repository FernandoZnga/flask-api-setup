""" Define el repositorio de Certificados """

from models import Certificado

class CertificadoRepository:
    """ El repositorio para el modelo de Certificados """

    @staticmethod
    def obtener_certificado():
        """ Consulta para obtener un certificado disponible para asignar """
        pass

    @staticmethod
    def listar_certificados():
        """ Consulta para listar todos los certificados disponibles """
        pass

    @staticmethod
    def crear_certificado():
        """ Asigna el salgo de un certiicado y lo relaciona a una persona """
        pass

    @staticmethod
    def actualizar_certificado():
        """ Actualiza el saldo de un certificado ya asignado """
        pass

    @staticmethod
    def eliminar_certificado():
        """ Elimina un certificado asignado y con saldo """
        pass