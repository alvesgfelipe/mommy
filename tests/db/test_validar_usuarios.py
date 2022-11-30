from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from mommy.models import Usuario


def selecionar_usuario_no_db(db: SQLAlchemy) -> Usuario:
    usuario = db.session.execute(db.select(Usuario)).one()[0]

    return usuario


def test_inserir_usuario_com_email_existente_retorna_erro(db: SQLAlchemy):
    usuario: Usuario = Usuario(
        nome="Clara",
        sobrenome="Isabelle Jaqueline Mendes",
        email=selecionar_usuario_no_db(db).email,
    )
    usuario.setar_senha("YTF3tyEhfS")

    erro = False
    try:
        db.session.add(usuario)
        db.session.commit()
    except IntegrityError:
        erro = True

    assert erro is True


def test_verificar_senha_incorreta_retorna_false(db: SQLAlchemy):
    assert selecionar_usuario_no_db(db).verificar_senha("senha-incorreta") is False


def test_verificar_senha_correta_retorna_true(db: SQLAlchemy):
    assert (
        selecionar_usuario_no_db(db).verificar_senha(selecionar_usuario_no_db(db).senha)
        is False
    )
