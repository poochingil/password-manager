<<<<<<< HEAD
from flask import Flask
from roles.routing.routes import blp as role_based_blueprint
from auth.routing.routes import blp as auth_operations_blueprint
from flask_smorest import Api
from db import db
import models
import os
from flask_jwt_extended import JWTManager


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Password Manager API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "poochi"
    jwt = JWTManager(app)

    with app.app_context():
        db.create_all()

    # with app.app_context():

    api.register_blueprint(role_based_blueprint)
    api.register_blueprint(auth_operations_blueprint)

    return app
=======
from flask import Flask
from roles.routing.routes import blp as role_based_blueprint
from auth.routing.routes import blp as auth_operations_blueprint
from flask_smorest import Api
from db import db
import models
import os
from flask_jwt_extended import JWTManager


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Password Manager API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "poochi"
    jwt = JWTManager(app)

    with app.app_context():
        db.create_all()

    # with app.app_context():

    api.register_blueprint(role_based_blueprint)
    api.register_blueprint(auth_operations_blueprint)

    return app
>>>>>>> origin/main
