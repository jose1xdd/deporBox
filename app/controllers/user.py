
from flask import request, Blueprint, jsonify
from app.models.modelos import User
from app.schemas.esquemas import userSchema
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
)

user_bp = Blueprint("user", __name__)


@user_bp.route("/register", methods=["GET", "POST"])
def signup_user():
    try:
        data = request.get_json()
        hashed_password = generate_password_hash(data["password"], method="sha256")
        new_user = User(
            id=data.get("id"),
            email=data.get("email"),
            password=hashed_password,
            admin=data.get("admin"),
        )
        new_user.save()
        userschema = userSchema()
        data = userschema.dump(new_user)
        return jsonify(data)
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@user_bp.route("/login", methods=["POST"])
def login_user():
    try:
        data = request.get_json()
        user = User.query.filter_by(email=data.get("email")).first()
        if check_password_hash(user.password, data.get("password")):
            access_token = create_access_token(user.password)
            refresh_token = create_refresh_token(user.password)
            return jsonify(access_token=access_token, refresh_token=refresh_token)
        else:
            return jsonify({"mesage": "credenciales invalidas"}), 401
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@user_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity, fresh=False)
    return jsonify(access_token=access_token)


@user_bp.route("/usuario", methods=["GET"])
@jwt_required()
def getUsuarios():
    try:
        recipe = User.get_all()
        usuarioschema = userSchema(many=True)
        data = usuarioschema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@user_bp.route("/usuario/<string:id>", methods=["GET"])
@jwt_required()
def getUsuario(id):
    try:
        recipe = User.get_by_id(id)
        usuarioschema = userSchema()
        data = usuarioschema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@user_bp.route("/usuario/<string:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    try:
        recipe = User.get_by_id(id)
        print(recipe)
        User.delete(recipe)
        usuarioschema = userSchema()
        data = usuarioschema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@user_bp.route("/usuario/<string:id>", methods=["PUT"])
@jwt_required()
def update(id):
    try:
        data = request.get_json()
        recipe = User.get_by_id(id)
        hashed_password = generate_password_hash(data["password"], method="sha256")
        recipe.password = hashed_password
        recipe.email = data.get("email")
        recipe.admin = data.get("admin")
        User.save(recipe)
        usuarioschema = userSchema()
        data = usuarioschema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500
