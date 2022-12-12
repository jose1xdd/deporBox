from app.db import db, crud


class User(db.Model, crud):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cedula = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    type_doc = db.Column(db.Text, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    fecha_nacimiento = db.Column(db.DateTime, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    direccion = db.Column(db.String(30), nullable=False)
    tests = db.relationship("Test", backref="user", lazy=True)
    binario = db.relationship(
        "binariosUsuarios", backref="user", lazy=True, uselist=False
    )


class Test(db.Model, crud):
    id = db.Column(db.Integer(), primary_key=True, nullable=False, autoincrement=True)
    trimestre = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.Date, nullable=False, unique=True)
    fuerza_general = db.Column(db.Integer, nullable=False)
    brazos = db.Column(db.Integer, nullable=False)
    piernas = db.Column(db.Integer, nullable=False)
    abdomen = db.Column(db.Integer, nullable=False)
    resistencia_fuerza = db.Column(db.Integer, nullable=False)
    resistencia_vueltas = db.Column(db.Integer, nullable=False)
    repeticiones = db.Column(db.Integer, nullable=False)
    resistencia_fuerzaG = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


class binariosUsuarios(db.Model, crud):
    id = db.Column(db.Integer(), primary_key=True, nullable=False, autoincrement=True)
    foto_perfil = db.Column(db.LargeBinary, nullable=True)
    foto_documento = db.Column(db.LargeBinary, nullable=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False, unique=True
    )
