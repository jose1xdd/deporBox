from flask import request, Blueprint, jsonify, make_response
from app.models.modelos import User
from app.schemas.esquemas import userSchema
from werkzeug.security import generate_password_hash, check_password_hash


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


@user_bp.route("/login", methods=["GET", "POST"])
def login_user():

    auth = request.authorization
    print(auth)

    if not auth or not auth.username or not auth.password:
        return make_response(
            "could not verify",
            401,
            {"WWW.Authentication": 'Basic realm: "login required"'},
        )

    user = User.query.filter_by(email=auth.username).first()
    print(user)

    if check_password_hash(user.password, auth.password):
        from main import app
        token = jwt.encode(
            
            {
                "id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            },
            
            app.config["SECRET_KEY"],
        )
        return jsonify({"token": token.decode("UTF-8")})

    return make_response(
        "could not verify", 401, {"WWW.Authentication": 'Basic realm: "login required"'}
    )
