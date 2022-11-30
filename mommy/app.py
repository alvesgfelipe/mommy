from configurar import setar_banco_de_dados, setar_config
from flask import Flask


def create_app(usar_pytest: bool = False) -> Flask:
    app = Flask(__name__)

    setar_config(app, usar_pytest)
    setar_banco_de_dados(app)

    return app
