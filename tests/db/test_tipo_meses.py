import datetime

from flask_sqlalchemy import SQLAlchemy

from mommy.models import Mes


def selecionar_mes_no_db(db: SQLAlchemy) -> Mes:
    mes = db.session.execute(db.select(Mes)).one()[0]

    return mes


def test_mes_id_retorna_str(db: SQLAlchemy):
    assert type(selecionar_mes_no_db(db).id) is str


def test_mes_data_retorna_datetime(db: SQLAlchemy):
    assert type(selecionar_mes_no_db(db).data) is datetime.datetime


def test_mes_usuarios_id_retorna_str(db: SQLAlchemy):
    assert type(selecionar_mes_no_db(db).usuarios_id) is str
