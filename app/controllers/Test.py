from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.models.modelos import Test
from app.schemas.esquemas import testSchema

test_bp = Blueprint('test_bp', __name__)

@test_bp.route('/test', methods=['POST'])
def crear():
    try:
        data = request.json
        recipe = Test(
            id =data.get('id'),
            trimestre= data.get('trimestre'),
            fuerza_general= data.get('fuerza_general'),
            brazos= data.get('brazos'),
            piernas= data.get('piernas'),
            abdomen= data.get('abdomen'),
            resistencia_fuerza= data.get('resistencia_fuerza'),
            resistencia_vueltas= data.get('resistencia_vueltas'),
            repeticiones= data.get('repeticiones'),
            resistencia_fuerzaG= data.get('resistencia_fuerzaG'),
            peso= data.get('peso'),
            persona_id=data.get('persona_id')
        )
        recipe.save()
        test_schema = testSchema()
        data = test_schema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500

@test_bp.route('/test/<int:id>', methods=['GET'])
def consultar_id(id):
    try:
        recipe = Test.get_by_id(id)
        test_schema = testSchema()
        data = test_schema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500


@test_bp.route('/test', methods=['GET'])
def consultar_all():
    try:
        recipe = Test.get_all()
        test_schema = testSchema(many=True)
        data = test_schema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500

@test_bp.route('/test/<int:id>', methods=['PUT'])
def update(id):
    try:
        recipe = Test.get_by_id(id)
        if recipe == None:
            return "El dato a editar no existe"
        else:
            data = request.json
            test_schema = testSchema()
            recipe.id =data.get('id')
            recipe.trimestre=data.get('trimestre')
            recipe.fuerza_general=data.get('fuerza_general')
            recipe.brazos=data.get('brazos')
            recipe.piernas=data.get('piernas')
            recipe.abdomen=data.get('abdomen')
            recipe.resistencia_fuerza=data.get('resistencia_fuerza')
            recipe.resistencia_vueltas=data.get('resistencia_vueltas')
            recipe.repeticiones=data.get('repeticiones')
            recipe.resistencia_fuerzaG=data.get('resistencia_fuerzaG')
            recipe.peso=data.get('peso')
            recipe.persona_id=data.get('persona_id')
            Test.save(recipe)
            data = test_schema.dump(recipe)
            return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500

@test_bp.route('/test/<int:id>', methods=['DELETE'])
def delete_id(id):
    try:
        recipe = Test.get_by_id(id)
        if recipe == None:
            return "El dato a eliminar no existe"
        else:
            Test.delete(recipe)
            test_schema = testSchema()
            data = test_schema.dump(recipe)
            return jsonify(data)
    except Exception as ex:
        return jsonify({'mesage': str(ex)}), 500