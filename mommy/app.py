from flask import Flask
from models import db


def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_prefixed_env()

    db.init_app(app)

    return app
