from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.models.modelos import Test
from app.schemas.esquemas import testSchema



@prueba_bp.route('/prueba/<int:id>', methods=['GET'])
def consultar_id(id):
    try:
        recipe = Producto.get_by_id(id)
        prueba_schema = pruebaSchema()
        data = prueba_schema.dump(recipe)
        print(data)
        return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500


@prueba_bp.route('/prueba', methods=['GET'])
def consultar_all():
    try:
        recipe = Producto.get_all()
        print(recipe)
        prueba_schema = pruebaSchema(many=True)
        data = prueba_schema.dump(recipe)
        print(data)
        return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500