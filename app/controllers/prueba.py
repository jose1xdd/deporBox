from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.models.prueba import Producto, Topos
from app.schemas.prueba import pruebaSchema, TopoSchema

prueba_bp = Blueprint('producto_bp', __name__)


@prueba_bp.route('/prueba', methods=['POST'])
def crear():
    try:
        data = request.json
        recipe = Producto(
            id=data.get('id'),
            nombre=data.get('nombre')
        )
        recipe.save()
        prueba_schema = pruebaSchema()
        data = prueba_schema.dump(recipe)
        print(data)
        return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500


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


@prueba_bp.route('/prueba/<int:id>', methods=['PUT'])
def update(id):
    try:
        recipe = Producto.get_by_id(id)
        if recipe == None:
            return "El dato a editar no existe"
        else:
            data = request.json
            prueba_schema = pruebaSchema()
            recipe.nombre = data.get('nombre')
            Producto.save(recipe)
            data = prueba_schema.dump(recipe)

            print(data)
            return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500


@prueba_bp.route('/prueba/<int:id>', methods=['DELETE'])
def delete_id(id):
    try:
        recipe = Producto.get_by_id(id)
        if recipe == None:
            return "El dato a eliminar no existe"
        else:
            Producto.delete(recipe)
            prueba_schema = pruebaSchema()
            data = prueba_schema.dump(recipe)
            print(data)
            return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500


@prueba_bp.route('/topo', methods=['POST'])
def crearTopo():
    try:
        data = request.json
        recipe = Topos(
            id=data.get('id'),
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            id_producto=data.get('id_producto')
        )
        recipe.save()
        prueba_schema = TopoSchema()
        data = prueba_schema.dump(recipe)
        print(data)
        return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500
