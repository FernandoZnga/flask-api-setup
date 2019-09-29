"""
Define el modelo de los puntos
"""
from . import db
from .abc import BaseModel

class Puntos(db.Model, BaseModel):
    """ El modelo de puntos """
    __tablename__ = 'puntos'

    id = db.Column(db.String(255), primary_key=True)
    codigo = db.Column(db.String(255), unique=True, nullable=False)
    estado = db.Column(db.String(255), nullable=False, default=1)
    puntos = db.Column(db.Integer, nullable=False, default=0)
    fechaCreacion = db.Column(db.DateTime, nullable=False)
    fechaActualizacion = db.Column(db.DateTime, nullable=False)
    fechaBorrado = db.Column(db.DateTime, nullable=False)

    def __init__(self, id, codigo, estado, monto, fechaCreacion, fechaActualizacion, fechaBorrado):
        """ Constructor de puntos """
        self.id = id
        self.codigo = codigo
        self.estado = estado
        self.puntos = puntos
        self.fechaCreacion = fechaCreacion
        self.fechaActualizacion = fechaActualizacion
        self.fechaBorrado = fechaBorrado