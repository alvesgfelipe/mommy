import pytest
from db.functions.povoar import povoar_banco_de_dados
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from mommy.app import create_app
from mommy.models import db as _db


@pytest.fixture(scope="module")
def app() -> Flask:
    app: Flask = create_app(usar_pytest=True)

    return app


@pytest.fixture(scope="module")
def db(app: Flask) -> SQLAlchemy:
    _db.init_app(app)

    with app.app_context():
        _db.drop_all()
        _db.create_all()

        povoar_banco_de_dados(_db)

        return _db
