from flask import Flask, jsonify
from app.db import db
from app.jwt import jwt
from app.controllers.user import user_bp
from app.controllers.binariosUsuario import binariosUsuario_bp
from app.controllers.Test import test_bp
from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from flask_migrate import Migrate
from flask_cors import CORS
def create_app(settings="config.default"):
    app = Flask(__name__)
    app.config.from_object((settings))
    db.init_app(app)
    jwt.init_app(app)
    app.url_map.strict_slashes = False
    app.register_blueprint(binariosUsuario_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(test_bp)
    register_error_handlers(app)
    migrate = Migrate(app, db)
    cors = CORS(app)
    return app



def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({"msg": e.args}), 500

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({"msg": "Method not allowed"}), 405

    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({"msg": "Forbidden error"}), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({"msg": "Not Found error"}), 404

    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({"msg": str(e)}), 500

    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({"msg": str(e)}), 404
