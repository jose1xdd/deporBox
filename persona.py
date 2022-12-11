from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_current_user
from app.jwt import auth
from app.models.modelos import Persona
from app.schemas.esquemas import personaSchema

persona_bp = Blueprint("persona_bp", __name__)


@persona_bp.route("/persona", methods=["POST"])
@jwt_required()
def crear():
    try:
        user = get_current_user()
        if auth(user):
            data = request.json
            recipe = Persona(
                type_doc=data.get("type_doc"),
                nombre=data.get("nombre"),
                fecha_nacimiento=data.get("fecha_nacimiento"),
                sexo=data.get("sexo"),
                direccion=data.get("direccion"),
            )
            recipe.save()
            persona_schema = personaSchema()
            data = persona_schema.dump(recipe)
            return jsonify(data)
        else:
            return jsonify({"message": "usuario no es admin"}), 401

    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@persona_bp.route("/persona/<string:id>", methods=["GET"])
@jwt_required()
def consultar_id(id):
    try:
        recipe = Persona.get_by_id(id)
        persona_schema = personaSchema()
        data = persona_schema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@persona_bp.route("/persona", methods=["GET"])
def consultar_all():
    try:
        user = get_current_user()
        if auth(user):
            recipe = Persona.get_all()
            persona_schema = personaSchema(many=True)
            data = persona_schema.dump(recipe)
            return jsonify(data)
        else:
            return jsonify({"message": "usuario no es admin"}), 401

    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@persona_bp.route("/persona/<string:id>", methods=["PUT"])
@jwt_required()
def update(id):
    try:
        user = get_current_user()
        if auth(user):
            recipe = Persona.get_by_id(id)
            data = request.json
            persona_schema = personaSchema()
            recipe.type_doc = data.get("type_doc")
            recipe.nombre = data.get("nombre")
            recipe.fecha_nacimiento = data.get("fecha_nacimiento")
            recipe.sexo = data.get("sexo")
            recipe.direccion = data.get("direccion")
            recipe.user_id = data.get("user_id")
            Persona.save(recipe)
            data = persona_schema.dump(recipe)
            return jsonify(data)
        else:
            return jsonify({"message": "usuario no es admin"}), 401

    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@persona_bp.route("/persona/<string:id>", methods=["DELETE"])
@jwt_required()
def delete_id(id):
    try:
        user = get_current_user()
        if auth(user):
            recipe = Persona.get_by_id(id)
            Persona.delete(recipe)
            persona_schema = personaSchema()
            data = persona_schema.dump(recipe)
            return jsonify(data)
        else:
            return jsonify({"message": "usuario no es admin"}), 401

    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500
