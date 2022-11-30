import datetime

from flask_sqlalchemy import SQLAlchemy

from mommy.models import Peca


def selecionar_peca_no_db(db: SQLAlchemy) -> Peca:
    peca = db.session.execute(db.select(Peca)).one()[0]

    return peca


def test_peca_id_retorna_int(db: SQLAlchemy):
    assert type(selecionar_peca_no_db(db).id) is int


def test_peca_data_retorna_datetime(db: SQLAlchemy):
    assert type(selecionar_peca_no_db(db).data) is datetime.datetime


def test_peca_nome_retorna_str(db: SQLAlchemy):
    assert type(selecionar_peca_no_db(db).nome) is str


def test_peca_pedra_retorna_int(db: SQLAlchemy):
    assert type(selecionar_peca_no_db(db).pedra) is int


def test_peca_valor_retorna_float(db: SQLAlchemy):
    assert type(selecionar_peca_no_db(db).valor) is float


def test_peca_total_peca_retorna_int(db: SQLAlchemy):
    assert type(selecionar_peca_no_db(db).total_peca) is int


def test_peca_total_pedra_retorna_int(db: SQLAlchemy):
    assert type(selecionar_peca_no_db(db).total_pedra) is int


def test_peca_lucro_retorna_float(db: SQLAlchemy):
    assert type(selecionar_peca_no_db(db).lucro) is float


def test_peca_usuarios_id_retorna_str(db: SQLAlchemy):
    assert type(selecionar_peca_no_db(db).usuarios_id) is str


def test_peca_meses_id_retorna_str(db: SQLAlchemy):
    assert type(selecionar_peca_no_db(db).meses_id) is str
