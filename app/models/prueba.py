from app.db import db, crud


class Producto(db.Model, crud):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), index=True)
    topos = db.relationship('Topos', backref='producto', lazy=True ,uselist=False)
    """
    uno a muchos
    topos = db.relationship('Topos', backref='producto', lazy=True)
    """


class Topos(db.Model, crud):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), index=True)
    apellido = db.Column(db.String(45), index=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False, unique=True)

    """
    uno a muchos
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    """
