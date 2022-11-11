from marshmallow import fields
from app.ext import ma

class personaSchema(ma.Schema):
    type_doc=fields.String()
    id=fields.String(dump_only=True)
    nombre=fields.String()
    fecha_nacimiento=fields.Date()
    sexo=fields.String()
    direccion=fields.String()
    email=fields.String()
    password=fields.String()
    tipo_usuario=fields.String()

class testSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    trimestre=fields.String()
    fuerza_general= fields.Integer()
    brazos= fields.Integer()
    piernas= fields.Integer()
    abdomen=fields.Integer()
    resistencia_fuerza=fields.Integer()
    resistencia_vueltas= fields.Integer()
    repeticiones= fields.Integer()
    resistencia_fuerzaG= fields.Integer()
    peso= fields.Integer()

class binariosUsuarioSchema(ma.Schema):
    foto_perfil=fields.Raw()
    foto_documento=fields.Raw()