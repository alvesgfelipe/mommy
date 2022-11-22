from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_prefixed_env()

    return app
