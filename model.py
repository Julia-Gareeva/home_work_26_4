from marshmallow import Schema, fields
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    """Модель класса пользователи."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(36), unique=True, nullable=False)
    password = db.Column(db.String(36), unique=True, nullable=False)


class UserSchema(Schema):
    """Схема сериализации класса пользователи."""
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
