from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_current_user
from app.jwt import auth
from app.models.modelos import Test
from app.schemas.esquemas import testSchema

test_bp = Blueprint("test_bp", __name__)


@test_bp.route("/test", methods=["POST"])
@jwt_required()
def crear():
    try:
        user = get_current_user()
        if auth(user):
            print("asdasd")
            data = request.json
            recipe = Test(
                trimestre=data.get("trimestre"),
                fuerza_general=data.get("fuerza_general"),
                brazos=data.get("brazos"),
                fecha=data.get("fecha"),
                piernas=data.get("piernas"),
                abdomen=data.get("abdomen"),
                resistencia_fuerza=data.get("resistencia_fuerza"),
                resistencia_vueltas=data.get("resistencia_vueltas"),
                resistencia_fuerzaG=data.get("resistencia_fuerzaG"),
                peso=data.get("peso"),
                user_id=data.get("user_id"),
            )
            
            recipe.save()
            test_schema = testSchema()
            data = test_schema.dump(recipe)
            return jsonify(data)
        else:
            return jsonify({"message": "usuario no es admin"}), 401
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@test_bp.route("/test/<int:id>", methods=["GET"])
@jwt_required()
def consultar_id(id):
    try:
        recipe = Test.get_by_id(id)
        test_schema = testSchema()
        data = test_schema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@test_bp.route("/test", methods=["GET"])
@jwt_required()
def consultar_all():
    try:
        recipe = Test.get_all()
        test_schema = testSchema(many=True)
        data = test_schema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@test_bp.route("/test/<int:id>", methods=["PUT"])
@jwt_required()
def update(id):
    try:
        user = get_current_user()
        if auth(user):
            recipe = Test.get_by_id(id)
            data = request.json
            test_schema = testSchema()
            recipe.trimestre = data.get("trimestre")
            recipe.fecha=data.get("fecha")
            recipe.fuerza_general = data.get("fuerza_general")
            recipe.brazos = data.get("brazos")
            recipe.piernas = data.get("piernas")
            recipe.abdomen = data.get("abdomen")
            recipe.resistencia_fuerza = data.get("resistencia_fuerza")
            recipe.resistencia_vueltas = data.get("resistencia_vueltas")
            recipe.resistencia_fuerzaG = data.get("resistencia_fuerzaG")
            recipe.peso = data.get("peso")
            Test.save(recipe)
            data = test_schema.dump(recipe)
            return jsonify(data)
        else:
            return jsonify({"message": "usuario no es admin"}), 401
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@test_bp.route("/test/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_id(id):
    try:

        user = get_current_user()
        if auth(user):
            recipe = Test.get_by_id(id)
            Test.delete(recipe)
            test_schema = testSchema()
            data = test_schema.dump(recipe)
            return jsonify(data)
        else:
            return jsonify({"message": "usuario no es admin"}), 401
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500
