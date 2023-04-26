<<<<<<< HEAD
import json
from flask_smorest import Blueprint, abort
from auth.signup import Signup
from models import RoleMappingModel, RoleModel
from util.util import user_signup_func, isAdmin
from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from schemas import AddWebsiteSchema, SignUpSchema, MakeAdminSchema, DeleteUserSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import db
from models.user_details import UserDetailModel
from datetime import datetime
from models.login import LoginModel

# import logging
#
#
# logging.basicConfig(filename="newfile.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')
#
# logger = logging.getLogger()
#
# logger.setLevel(logging.DEBUG)

blp = Blueprint("role", __name__, description="role based functionalities")


# admin endpoints
@blp.get("/admin/users")
@jwt_required()
def view_users_in_api():
    user_id = get_jwt_identity()
    response = []
    if isAdmin(user_id):
        all_values = LoginModel.query.all()
        for obj in all_values:
            response.append(obj.username)
    else:
        return {"message": "admin access only"}
    return response


@blp.post("/admin/users")
@blp.arguments(SignUpSchema)
@jwt_required()
def add_user_in_api(data):
    user_id = get_jwt_identity()

    if isAdmin(user_id):
        username = data["username"]
        password = data["password"]
        email = data["email"]
        phone_number = data["phone_number"]

        data_to_append = Signup.signup_func(username, password, email, phone_number)
        item = LoginModel(**data_to_append)
        role = RoleModel.query.get_or_404(2)

        item.user_var.append(role)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            return {"message": "user already exists"}, 200
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")
    else:
        return {"message": "admin access only"}
    return {"message": "user created"}


@blp.put("/admin/<int:user_id>/make_admin")
@jwt_required()
def make_admin(user_id):
    admin_id = get_jwt_identity()
    user = LoginModel.query.get_or_404(user_id)
    if isAdmin(admin_id):

        if RoleMappingModel.query.filter_by(user_id=user_id).first().role_id == 2:
            RoleMappingModel.query.filter_by(user_id=user_id).first().role_id = 1
            db.session.commit()
            print(RoleMappingModel.query.filter_by(user_id=user_id).first().role_id)
            return {"message": "admin made successfully"}
        else:
            return {"message": "already admin"}
    else:
        return {"message": "admin access only"}


@blp.delete("/admin/<int:user_id>/users")
@jwt_required()
def remove_user_in_api(user_id):
    admin_id = get_jwt_identity()
    user = LoginModel.query.get_or_404(user_id)
    if isAdmin(admin_id):
        if RoleMappingModel.query.filter_by(user_id=user_id).first().role_id == 2:
            row_to_be_removed1 = UserDetailModel.query.filter_by(user_id=user_id)
            row_to_be_removed2 = LoginModel.query.filter_by(id=user_id).first()
            if row_to_be_removed1 is not None:
                row_to_be_removed1.delete()
                db.session.delete(row_to_be_removed2)
            else:
                db.session.delete(row_to_be_removed2)
            db.session.commit()
            return {"message": "user removed"}
        else:
            return {"message": "Can't remove admin"}
    else:
        return {"message": "admin access only"}


# user endpoints
@blp.get("/user/websites")
@jwt_required()
def view_website_in_api():
    user_id = get_jwt_identity()
    result_obj = UserDetailModel.query.filter_by(user_id=user_id).all()
    response = []
    for obj in result_obj:
        response.extend([obj.website, obj.password, obj.username])
    return response


@blp.post("/user/websites")
@blp.arguments(AddWebsiteSchema)
@jwt_required()
def add_website_in_api(data):
    data["user_id"] = get_jwt_identity()
    date = datetime.now()
    data["creation_date"] = date.strftime("%d/%m/%y")
    item = UserDetailModel(**data)

    try:
        db.session.add(item)
        db.session.commit()
    except IntegrityError:
        return {"message": "username already exists for this website"}, 200
    except SQLAlchemyError:
        abort(500, message="An error occurred while inserting the item.")

    return {"message": "done"}
=======
import json
from flask_smorest import Blueprint, abort
from auth.signup import Signup
from models import RoleMappingModel, RoleModel
from util.util import user_signup_func, isAdmin
from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from schemas import AddWebsiteSchema, SignUpSchema, MakeAdminSchema, DeleteUserSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import db
from models.user_details import UserDetailModel
from datetime import datetime
from models.login import LoginModel

# import logging
#
#
# logging.basicConfig(filename="newfile.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')
#
# logger = logging.getLogger()
#
# logger.setLevel(logging.DEBUG)

blp = Blueprint("role", __name__, description="role based functionalities")


# admin endpoints
@blp.get("/admin/users")
@jwt_required()
def view_users_in_api():
    user_id = get_jwt_identity()
    response = []
    if isAdmin(user_id):
        all_values = LoginModel.query.all()
        for obj in all_values:
            response.append(obj.username)
    else:
        return {"message": "admin access only"}
    return response


@blp.post("/admin/users")
@blp.arguments(SignUpSchema)
@jwt_required()
def add_user_in_api(data):
    user_id = get_jwt_identity()

    if isAdmin(user_id):
        username = data["username"]
        password = data["password"]
        email = data["email"]
        phone_number = data["phone_number"]

        data_to_append = Signup.signup_func(username, password, email, phone_number)
        item = LoginModel(**data_to_append)
        role = RoleModel.query.get_or_404(2)

        item.user_var.append(role)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            return {"message": "user already exists"}, 200
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")
    else:
        return {"message": "admin access only"}
    return {"message": "user created"}


@blp.put("/admin/<int:user_id>/make_admin")
@jwt_required()
def make_admin(user_id):
    admin_id = get_jwt_identity()
    user = LoginModel.query.get_or_404(user_id)
    if isAdmin(admin_id):

        if RoleMappingModel.query.filter_by(user_id=user_id).first().role_id == 2:
            RoleMappingModel.query.filter_by(user_id=user_id).first().role_id = 1
            db.session.commit()
            print(RoleMappingModel.query.filter_by(user_id=user_id).first().role_id)
            return {"message": "admin made successfully"}
        else:
            return {"message": "already admin"}
    else:
        return {"message": "admin access only"}


@blp.delete("/admin/<int:user_id>/users")
@jwt_required()
def remove_user_in_api(user_id):
    admin_id = get_jwt_identity()
    user = LoginModel.query.get_or_404(user_id)
    if isAdmin(admin_id):
        if RoleMappingModel.query.filter_by(user_id=user_id).first().role_id == 2:
            row_to_be_removed1 = UserDetailModel.query.filter_by(user_id=user_id)
            row_to_be_removed2 = LoginModel.query.filter_by(id=user_id).first()
            if row_to_be_removed1 is not None:
                row_to_be_removed1.delete()
                db.session.delete(row_to_be_removed2)
            else:
                db.session.delete(row_to_be_removed2)
            db.session.commit()
            return {"message": "user removed"}
        else:
            return {"message": "Can't remove admin"}
    else:
        return {"message": "admin access only"}


# user endpoints
@blp.get("/user/websites")
@jwt_required()
def view_website_in_api():
    user_id = get_jwt_identity()
    result_obj = UserDetailModel.query.filter_by(user_id=user_id).all()
    response = []
    for obj in result_obj:
        response.extend([obj.website, obj.password, obj.username])
    return response


@blp.post("/user/websites")
@blp.arguments(AddWebsiteSchema)
@jwt_required()
def add_website_in_api(data):
    data["user_id"] = get_jwt_identity()
    date = datetime.now()
    data["creation_date"] = date.strftime("%d/%m/%y")
    item = UserDetailModel(**data)

    try:
        db.session.add(item)
        db.session.commit()
    except IntegrityError:
        return {"message": "username already exists for this website"}, 200
    except SQLAlchemyError:
        abort(500, message="An error occurred while inserting the item.")

    return {"message": "done"}
>>>>>>> origin/main
