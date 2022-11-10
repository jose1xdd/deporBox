from app.db import db, crud

class Persona(db.Model, crud):
    type_doc = db.Column(db.Text, nullable=False)
    id= db.Colum(db.Text, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    fecha_nacimiento = db.Column(db.DateTime, nullable=False)
    sexo= db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(30), nullable=False)
    email=db.Column(db.Text, nullable=False)
    password=db.Column(db.Text, nullable=False)
    tipo_usuario=db.Column(db.String(1), nullable=False)
    child_binUser=db.relationship('binariosUsuarios', backref='persona', uselist=False)
    child_tests=db.relationship('Test', backref='persona', lazy=True)

class binariosUsuarios(db.Model, crud):
    foto_perfil=db.Column(db.LargeBinary, nullable=False)
    foto_documento=db.Column(db.LargeBinary, nullable=False)
    id_persona = db.Column(db.Text, db.ForeignKey('persona.id'), nullable=False, primary_key=True)

class Test(db.Model, crud):
    id =db.Column(db.Integer, primary_hey=True, nullable=False)
    trimestre=db.Column(db.Text, nullable=False)
    fuerza_general=db.Column(db.Integer, nullable=False)
    brazos=db.Column(db.Integer, nullable=False)
    piernas=db.Column(db.Integer, nullable=False)
    abdomen=db.Column(db.Integer, nullable=False)
    resistencia_fuerza=db.Column(db.Integer, nullable=False)
    resistencia_vueltas=db.Column(db.Integer, nullable=False)
    repeticiones=db.Column(db.Integer, nullable=False)
    resistencia_fuerzaG=db.Column(db.Integer, nullable=False)
    peso=db.Column(db.Integer, nullable=False)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)