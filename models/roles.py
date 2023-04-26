<<<<<<< HEAD
from db import db


class RoleModel(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(180), unique=True, nullable=False)

    # role_mapping_var = db.relationship("RoleMappingModel", back_populates="role")
=======
from db import db


class RoleModel(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(180), unique=True, nullable=False)

    # role_mapping_var = db.relationship("RoleMappingModel", back_populates="role")
>>>>>>> origin/main
    login = db.relationship("LoginModel", back_populates="user_var", secondary="role_mapping")