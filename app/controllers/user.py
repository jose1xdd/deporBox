from flask import request, Blueprint, jsonify
from app.models.modelos import User
from app.schemas.esquemas import userSchema
from app.jwt import auth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_current_user,
)

user_bp = Blueprint("user", __name__)


@user_bp.route("/register", methods=["GET", "POST"])
def signup_user():
    try:
        data = request.get_json()
        hashed_password = generate_password_hash(data["password"], method="sha256")
        new_user = User(
            email=data.get("email"),
            password=hashed_password,
            admin=data.get("admin"),
            type_doc=data.get("type_doc"),
            nombre=data.get("nombre"),
            fecha_nacimiento=data.get("fecha_nacimiento"),
            sexo=data.get("sexo"),
            direccion=data.get("direccion"),
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
            access_token = create_access_token(user.email)
            refresh_token = create_refresh_token(user.email)
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
        user = get_current_user()
        if auth(user):
            recipe = User.get_all()
            usuarioschema = userSchema(many=True)
            data = usuarioschema.dump(recipe)
            return jsonify(data)
        else:
            return jsonify({"message": "usuario no es admin"}), 401
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@user_bp.route("/usuario/<string:data>", methods=["GET"])
@jwt_required()
def getUsuarioemail(data):
    try:
        recipe = User.query.filter_by(email=data).first()
        usuarioschema = userSchema()
        data = usuarioschema.dump(recipe)
        return jsonify(data)
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500



@user_bp.route("/usuario/<string:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    try:
        user = get_current_user()
        if auth(user):
            recipe = User.get_by_id(id)
            User.delete(recipe)
            usuarioschema = userSchema()
            data = usuarioschema.dump(recipe)
            return jsonify(data)
        else:
            return jsonify({"message": "usuario no es admin"}), 401
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500


@user_bp.route("/usuario/<string:id>", methods=["PUT"])
@jwt_required()
def update(id):
    try:
        user = get_current_user()
        if auth(user):
            data = request.get_json()
            recipe = User.get_by_id(id)
            hashed_password = generate_password_hash(data["password"], method="sha256")
            recipe.password = hashed_password
            recipe.email = data.get("email")
            recipe.admin = data.get("admin")
            recipe.type_doc = data.get("type_doc")
            recipe.nombre = data.get("nombre")
            recipe.fecha_nacimiento = data.get("fecha_nacimiento")
            recipe.sexo = data.get("sexo")
            recipe.direccion = data.get("direccion")
            User.save(recipe)
            usuarioschema = userSchema()
            data = usuarioschema.dump(recipe)
            return jsonify(data)
        else:
            return jsonify({"message": "usuario no es admin"}), 401
    except Exception as ex:
        return jsonify({"mesage": str(ex)}), 500
