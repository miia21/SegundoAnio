from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class paquete(db.Model):
    __tablename__="paquete"
    id=db.Column(db.Integer, primary_key=True)
    numeroenvio=db.Column(db.Integer, unique=True, nullable=False)
    peso=db.Column(db.Float, nullable=False)
    nomdestinatario=db.Column(db.String(80), nullable=False)
    dirdestinatario=db.Column(db.String(120), nullable=False)
    entregado=db.Column(db.Boolean, nullable=False)
    observaciones=db.Column(db.Text)
    idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    idtransporte=db.Column(db.Integer, db.ForeignKey('transporte.id'))
    idrepartidor=db.Column(db.Integer, db.ForeignKey('repartidor.id'))

class repartidor(db.Model):
    __tablename__="repartidor"
    id=db.Column(db.Integer, primary_key=True)
    numero=db.Column(db.Integer, unique=True, nullable=False)
    nombre=db.Column(db.String(80), nullable=False)
    dni=db.Column(db.String(8), nullable=False)
    idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'))

class sucursal(db.Model):
    __tablename__="sucursal"
    id=db.Column(db.Integer, primary_key=True)
    numero=db.Column(db.Integer, unique=True, nullable=False)
    provincia=db.Column(db.String(80), nullable=False)
    localidad=db.Column(db.String(80), nullable=False)
    direccion=db.Column(db.String(120), nullable=False)

class transporte(db.Model):
    __tablename__="transporte"
    id = db.Column(db.Integer, primary_key=True)
    numerotransporte=db.Column(db.Integer, unique=True, nullable=False)
    fechahorasalida=db.Column(db.DateTime)
    fechahorallegada=db.Column(db.DateTime)
    idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'))
