<<<<<<< HEAD
from db import db


class RoleMappingModel(db.Model):
    __tablename__ = "role_mapping"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("login.id"), unique=False, nullable=False
    )
    role_id = db.Column(
        db.Integer, db.ForeignKey("roles.id"), unique=False, nullable=False
    )

    # role = db.relationship("RoleModel", back_populates="role_mapping_var")
=======
from db import db


class RoleMappingModel(db.Model):
    __tablename__ = "role_mapping"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("login.id"), unique=False, nullable=False
    )
    role_id = db.Column(
        db.Integer, db.ForeignKey("roles.id"), unique=False, nullable=False
    )

    # role = db.relationship("RoleModel", back_populates="role_mapping_var")
>>>>>>> origin/main
