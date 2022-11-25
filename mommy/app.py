from flask import Flask
from models import db


def create_app(usar_pytest: bool = False) -> Flask:
    app: Flask = Flask(__name__)

    if usar_pytest:
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["TESTING"] = True
    else:
        app.config.from_prefixed_env()

    db.init_app(app)

    return app
