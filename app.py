from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api
from default_config import Config
from main import users_ns
from model import db


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def create_data(app, db):
    with app.app_context():
        db.create_all()


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(users_ns)
    create_data(app, db)


app = create_app(Config())
app.debug = True
migrate = Migrate(app, db, render_as_batch=True)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="localhost", port=80, debug=True)
