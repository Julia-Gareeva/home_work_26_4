from hashlib import md5
from flask import request
from flask_restx import Resource, Namespace
from model import db
from model import User

users_ns = Namespace('users')


@users_ns.route('/')
class UserView(Resource):
    def get(self):
        """Метод для получения всех пользователей."""

        users = User.query.all()
        response = {
            "total": len(users),
            "users": [{"username": user.username} for user in users],
        }

        return response, 200


@users_ns.route('/register/')
class UsersViews(Resource):
    def post(self):
        """Метод для создания нового пользователя."""

        user_data = request.json
        new = User(
            username=user_data["username"],
            password=md5(user_data["password"].encode()).hexdigest()
            )
        db.session.add(new)
        db.session.commit()

        return '', 201, {'location': f'/users/{User.id}'}
