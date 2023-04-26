<<<<<<< HEAD
from db import db
from sqlalchemy import UniqueConstraint


class UserDetailModel(db.Model):
    __tablename__ = "user_details"
    __table_args__ = (
        UniqueConstraint("user_id", "website", "username"),
    )
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("login.id"), unique=False, nullable=False
    )
    website = db.Column(db.String(120), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(256), unique=False, nullable=False)
    modified_date = db.Column(db.String(256), unique=False, nullable=True)
    creation_date = db.Column(db.String(256), unique=False, nullable=True)

    login = db.relationship("LoginModel", back_populates="user")
=======
from db import db
from sqlalchemy import UniqueConstraint


class UserDetailModel(db.Model):
    __tablename__ = "user_details"
    __table_args__ = (
        UniqueConstraint("user_id", "website", "username"),
    )
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("login.id"), unique=False, nullable=False
    )
    website = db.Column(db.String(120), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(256), unique=False, nullable=False)
    modified_date = db.Column(db.String(256), unique=False, nullable=True)
    creation_date = db.Column(db.String(256), unique=False, nullable=True)

    login = db.relationship("LoginModel", back_populates="user")
>>>>>>> origin/main
