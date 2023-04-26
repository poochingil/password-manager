<<<<<<< HEAD
from db import db


class LoginModel(db.Model):
    __tablename__ = "login"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Integer, unique=False, nullable=False)
    # role_id = db.Column(
    #     db.Integer, db.ForeignKey("roles.id"), unique=False, nullable=False
    # )
    email = db.Column(db.String(180), unique=False, nullable=False)
    phone_number = db.Column(db.String(180), unique=False, nullable=False)

    user = db.relationship("UserDetailModel", back_populates="login")
    user_var = db.relationship("RoleModel", back_populates="login", secondary="role_mapping")

=======
from db import db


class LoginModel(db.Model):
    __tablename__ = "login"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Integer, unique=False, nullable=False)
    # role_id = db.Column(
    #     db.Integer, db.ForeignKey("roles.id"), unique=False, nullable=False
    # )
    email = db.Column(db.String(180), unique=False, nullable=False)
    phone_number = db.Column(db.String(180), unique=False, nullable=False)

    user = db.relationship("UserDetailModel", back_populates="login")
    user_var = db.relationship("RoleModel", back_populates="login", secondary="role_mapping")

>>>>>>> origin/main
