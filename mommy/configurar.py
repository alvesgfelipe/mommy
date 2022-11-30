from flask import Flask
from models import db


def setar_config(app: Flask, usar_pytest: bool = False):
    if usar_pytest:
        app.config["DEBUG"] = False
        app.config["SECRET_KEY"] = "8bf537e065687ad06c51ecdbedb992ce"
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["TESTING"] = True
    else:
        app.config.from_prefixed_env()


def setar_banco_de_dados(app: Flask):
    db.init_app(app)
