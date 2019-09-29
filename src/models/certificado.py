"""
Define el modelo de los certificados
"""
from . import db
from .abc import BaseModel


class Certificado(db.Model, BaseModel):
    """ El modelo de certificado """
    __tablename__ = 'certificado'

    id = db.Column(db.String(255), primary_key=True)
    codigo = db.Column(db.String(255), unique=True, nullable=False)
    estado = db.Column(db.String(255), nullable=False, default=1)
    monto = db.Column(db.Integer, nullable=False, default=0)
    fechaCreacion = db.Column(db.DateTime, nullable=False)
    fechaActualizacion = db.Column(db.DateTime, nullable=False)
    fechaBorrado = db.Column(db.DateTime, nullable=False)

    def __init__(self, id, codigo, estado, monto, fechaCreacion, fechaActualizacion, fechaBorrado):
        """ Create a new Certificado """
        self.id = id
        self.codigo = codigo
        self.estado = estado
        self.monto = monto
        self.fechaCreacion = fechaCreacion
        self.fechaActualizacion = fechaActualizacion
        self.fechaBorrado = fechaBorrado