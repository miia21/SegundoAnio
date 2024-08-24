
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()


class Paquete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numeroenvio = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    nomdestinatario = db.Column(db.String(60), nullable=False)
    dirdestinatario = db.Column(db.String(100), nullable=False)
    entregado = db.Column(db.Boolean, nullable=False)
    observaciones = db.Column(db.Text, nullable=False)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'))
    idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'))

class Repartidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(60), nullable=False)
    dni = db.Column(db.String(8), nullable=False)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))

class Transporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numerotransporte = db.Column(db.Integer, nullable=False)
    fechahorasalida = db.Column(db.DateTime)
    fechahorallegada = db.Column(db.DateTime)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))

class Sucursal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    provincia = db.Column(db.String(30), nullable=False)
    localidad = db.Column(db.String(30), nullable=False)
    direccion = db.Column(db.String(60), nullable=False)