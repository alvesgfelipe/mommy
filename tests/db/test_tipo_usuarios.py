from flask_sqlalchemy import SQLAlchemy

from mommy.models import Usuario


def selecionar_usuario_no_db(db: SQLAlchemy) -> Usuario:
    usuario = db.session.execute(db.select(Usuario)).one()[0]

    return usuario


def test_usuario_id_retorna_str(db: SQLAlchemy):
    assert type(selecionar_usuario_no_db(db).id) is str


def test_usuario_nome_retorna_str(db: SQLAlchemy):
    assert type(selecionar_usuario_no_db(db).nome) is str


def test_usuario_sobrenome_retorna_str(db: SQLAlchemy):
    assert type(selecionar_usuario_no_db(db).sobrenome) is str


def test_usuario_email_retorna_str(db: SQLAlchemy):
    assert type(selecionar_usuario_no_db(db).email) is str


def test_usuario_senha_retorna_bytes(db: SQLAlchemy):
    assert type(selecionar_usuario_no_db(db).senha) is bytes
