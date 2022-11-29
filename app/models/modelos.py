from app.db import db, crud

class Persona(db.Model, crud):
    type_doc = db.Column(db.Text, nullable=False)
    id = db.Column(db.String(30), primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    fecha_nacimiento = db.Column(db.DateTime, nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(30), nullable=False)
    tests = db.relationship("Test", backref="persona", lazy=True)
    binario = db.relationship(
        "binariosUsuarios", backref="persona", lazy=True, uselist=False
    )
    user_id = db.Column(db.String(30), db.ForeignKey("user.id"), nullable=False)


class User(db.Model, crud):
    id = db.Column(db.String(30), primary_key=True)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    persona = db.relationship("Persona", backref="user", lazy=True, uselist=False)


class Test(db.Model, crud):
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    trimestre = db.Column(db.Text, nullable=False)
    fuerza_general = db.Column(db.Integer, nullable=False)
    brazos = db.Column(db.Integer, nullable=False)
    piernas = db.Column(db.Integer, nullable=False)
    abdomen = db.Column(db.Integer, nullable=False)
    resistencia_fuerza = db.Column(db.Integer, nullable=False)
    resistencia_vueltas = db.Column(db.Integer, nullable=False)
    repeticiones = db.Column(db.Integer, nullable=False)
    resistencia_fuerzaG = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    persona_id = db.Column(db.String(30), db.ForeignKey("persona.id"), nullable=False)


class binariosUsuarios(db.Model, crud):
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    foto_perfil = db.Column(db.LargeBinary, nullable=True)
    foto_documento = db.Column(db.LargeBinary, nullable=True)
    persona_id = db.Column(
        db.String(30), db.ForeignKey("persona.id"), nullable=False, unique=True
    )
