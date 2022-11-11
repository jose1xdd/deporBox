from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.models.modelos import Persona
from app.schemas.esquemas import personaSchema

persona_bp = Blueprint('persona_bp', __name__)

@persona_bp.route('/persona', methods=['POST'])
def crear():
    try:
        data = request.json
        recipe = Persona(
            type_doc = data.get('type_doc'),
            id = data.get('id'),
            nombre = data.get('nombre'),
            fecha_nacimiento = data.get('fecha_nacimiento'),
            sexo = data.get('sexo'),
            direccion = data.get('direccion'),
            email = data.get('email'),
            password = data.get('password'),
            tipo_usuario = data.get('tipo_usuario')
        )
        recipe.save()
        persona_schema = personaSchema()
        data = persona_schema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500

@persona_bp.route('/persona/<string:id>', methods=['GET'])
def consultar_id(id):
    try:
        recipe = Persona.get_by_id(id)
        persona_schema = personaSchema()
        data = persona_schema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500


@persona_bp.route('/persona', methods=['GET'])
def consultar_all():
    try:
        recipe = Persona.get_all()
        persona_schema = personaSchema(many=True)
        data = persona_schema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500

@persona_bp.route('/persona/<string:id>', methods=['PUT'])
def update(id):
    try:
        recipe = Persona.get_by_id(id)
        if recipe == None:
            return "El dato a editar no existe"
        else:
            data = request.json
            persona_schema = personaSchema()
            recipe.type_doc = data.get('type_doc')
            recipe.id = data.get('id')
            recipe.nombre = data.get('nombre')
            recipe.fecha_nacimiento = data.get('fecha_nacimiento')
            recipe.sexo = data.get('sexo')
            recipe.direccion = data.get('direccion')
            recipe.email = data.get('email')
            recipe.password = data.get('password')
            recipe.tipo_usuario = data.get('tipo_usuario')
            Persona.save(recipe)
            data = persona_schema.dump(recipe)
            return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500

@persona_bp.route('/persona/<string:id>', methods=['DELETE'])
def delete_id(id):
    try:
        recipe = Persona.get_by_id(id)
        if recipe == None:
            return "El dato a eliminar no existe"
        else:
            Persona.delete(recipe)
            persona_schema = personaSchema()
            data = persona_schema.dump(recipe)
            return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500        