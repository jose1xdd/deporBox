from marshmallow import fields
from app.ext import ma


class pruebaSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()
    topos = fields.Nested('TopoSchema')
    """
    uno a muchos
    topos = fields.Nested('TopoSchema',many=True)
    """


class TopoSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()
    apellido = fields.String()
