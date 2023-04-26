<<<<<<< HEAD
from flask_smorest import Blueprint, abort
from auth.login import Login
from auth.signup import Signup
from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from models import RoleModel
from schemas import SignUpSchema, LoginSchema
import sqlite3
from flask_jwt_extended import create_access_token
from db import db
from models.login import LoginModel

blp = Blueprint("auth", __name__, description="auth operations ")


@blp.post('/auth/signup')
@blp.arguments(SignUpSchema)
def signup(data):
    username = data["username"]
    password = data["password"]
    email = data["email"]
    phone_number = data["phone_number"]

    user_data = Signup.signup_func(username, password, email, phone_number)
    item = LoginModel(**user_data)
    role = RoleModel.query.get_or_404(2)

    item.user_var.append(role)
    try:
        db.session.add(item)
        db.session.commit()
    except IntegrityError:
        return {"message": "user already exists"}, 200
    except SQLAlchemyError as e:
        print(e)
        abort(500, message="An error occurred while inserting the item.")

    return {"message": "done"}


@blp.post('/auth/login')
@blp.arguments(LoginSchema)
def login(data):
    user = LoginModel.query.filter(
        LoginModel.username == data["username"]).first()

    if user and Login.login(data["password"]):
        access_token = create_access_token(identity=user.id)
        return access_token
    return {"message": "user not found"}, 404
=======
from flask_smorest import Blueprint, abort
from auth.login import Login
from auth.signup import Signup
from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from models import RoleModel
from schemas import SignUpSchema, LoginSchema
import sqlite3
from flask_jwt_extended import create_access_token
from db import db
from models.login import LoginModel

blp = Blueprint("auth", __name__, description="auth operations ")


@blp.post('/auth/signup')
@blp.arguments(SignUpSchema)
def signup(data):
    username = data["username"]
    password = data["password"]
    email = data["email"]
    phone_number = data["phone_number"]

    user_data = Signup.signup_func(username, password, email, phone_number)
    item = LoginModel(**user_data)
    role = RoleModel.query.get_or_404(2)

    item.user_var.append(role)
    try:
        db.session.add(item)
        db.session.commit()
    except IntegrityError:
        return {"message": "user already exists"}, 200
    except SQLAlchemyError as e:
        print(e)
        abort(500, message="An error occurred while inserting the item.")

    return {"message": "done"}


@blp.post('/auth/login')
@blp.arguments(LoginSchema)
def login(data):
    user = LoginModel.query.filter(
        LoginModel.username == data["username"]).first()

    if user and Login.login(data["password"]):
        access_token = create_access_token(identity=user.id)
        return access_token
    return {"message": "user not found"}, 404
>>>>>>> origin/main
