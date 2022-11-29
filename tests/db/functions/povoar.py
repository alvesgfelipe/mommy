from flask_sqlalchemy import SQLAlchemy

from mommy.models import Mes, Peca, Usuario


def inserir_usuario_no_db(db: SQLAlchemy):
    usuario: Usuario = Usuario(
        nome="Kaique",
        sobrenome="Ricardo Raul Jesus",
        email="kaique_jesus@teadit.com.br",
    )
    usuario.setar_senha("pBkBqNiONT")

    db.session.add(usuario)
    db.session.commit()


def receber_id_do_usuario(db: SQLAlchemy) -> str:
    usuario: Usuario = db.session.execute(
        db.select(Usuario).filter_by(email="kaique_jesus@teadit.com.br")
    ).one()[0]

    return usuario.id


def inserir_mes_no_db(db: SQLAlchemy):
    mes: Mes = Mes(usuarios_id=receber_id_do_usuario(db))

    db.session.add(mes)
    db.session.commit()


def inserir_peca_no_db(db: SQLAlchemy):
    ultimo_mes: Mes = db.session.execute(
        db.select(Mes).filter_by(usuarios_id=receber_id_do_usuario(db))
    ).all()[-1][0]

    peca: Peca = Peca(nome="Estrela", pedra=10, valor=0.025, total_peca=5)
    peca.total_pedra = peca.pedra * peca.total_peca
    peca.lucro = peca.valor * peca.total_pedra
    peca.usuarios_id = receber_id_do_usuario(db)
    peca.meses_id = ultimo_mes.id

    db.session.add(peca)
    db.session.commit()


def povoar_banco_de_dados(db: SQLAlchemy):
    inserir_usuario_no_db(db)
    inserir_mes_no_db(db)
    inserir_peca_no_db(db)
