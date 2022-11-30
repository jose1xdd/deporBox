from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.models.modelos import binariosUsuarios
from app.schemas.esquemas import binariosUsuarioSchema

binariosUsuario_bp = Blueprint('binariosUsuario_bp', __name__)

@binariosUsuario_bp.route('/binariosUsuario', methods=['POST'])
@jwt_required()
def crear():
    try:
        data = request.json
        recipe = binariosUsuarios(
            foto_perfil=data.get('foto_perfil'),
            foto_documento=data.get('foto_documento'),
            persona_id=data.get('persona_id')
        )
        recipe.save()
        binariosUsuario_schema = binariosUsuarioSchema()
        data = binariosUsuario_schema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500

@binariosUsuario_bp.route('/binariosUsuario/<int:id>', methods=['GET'])
@jwt_required()
def consultar_id(id):
    try:
        recipe = binariosUsuarios.get_by_id(id)
        binariosUsuario_schema = binariosUsuarioSchema()
        data = binariosUsuario_schema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500


@binariosUsuario_bp.route('/binariosUsuario', methods=['GET'])
@jwt_required()
def consultar_all():
    try:
        recipe = binariosUsuarios.get_all()
        binariosUsuario_schema = binariosUsuarioSchema(many=True)
        data = binariosUsuario_schema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500

@binariosUsuario_bp.route('/binariosUsuario/<int:id>', methods=['PUT'])
@jwt_required()
def update(id):
    try:
        recipe = binariosUsuarios.get_by_id(id)
        data = request.json
        binariosUsuario_schema = binariosUsuarioSchema()
        recipe.foto_perfil=data.get('foto_perfil')
        recipe.foto_documento=data.get('foto_documento')
        recipe.persona_id=data.get('persona_id')
        binariosUsuarios.save(recipe)
        data = binariosUsuario_schema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500

@binariosUsuario_bp.route('/binariosUsuario/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_id(id):
    try:
        recipe = binariosUsuarios.get_by_id(id)
        if recipe == None:
            return "El dato a eliminar no existe"
        else:
            binariosUsuarios.delete(recipe)
            binariosUsuario_schema = binariosUsuarioSchema()
            data = binariosUsuario_schema.dump(recipe)
            return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500        