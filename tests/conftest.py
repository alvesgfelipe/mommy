import pytest
from flask import Flask

from mommy.app import create_app


@pytest.fixture(scope="module")
def app() -> Flask:
    app: Flask = create_app(usar_pytest=True)

    return app
