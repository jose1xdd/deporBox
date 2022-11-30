from flask_jwt_extended import JWTManager
from app.models.modelos import User

jwt = JWTManager()


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(email=identity).one_or_none()


def auth(user):
        if not user.admin == True:
            return False
        return True
 
