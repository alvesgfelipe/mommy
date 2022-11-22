from datetime import datetime
from uuid import uuid4

from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()


def gerar_uuid():
    return str(uuid4())


class Usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"

    id = db.Column(db.CHAR(36), primary_key=True, default=gerar_uuid)
    nome = db.Column(db.String(32), nullable=False)
    sobrenome = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(254), nullable=False, unique=True)
    senha = db.Column(db.CHAR(60), nullable=False)

    def setar_senha(self, senha_digitada: str):
        self.password = generate_password_hash(senha_digitada)

    def verificar_senha(self, senha_digitada: str):
        return check_password_hash(pw_hash=self.password, password=senha_digitada)


class Mes(db.Model):
    __tablename__ = "meses"

    id = db.Column(db.CHAR(36), primary_key=True, default=gerar_uuid)
    data = db.Column(db.DateTime, nullable=False, default=datetime.now)

    usuarios_id = db.Column(db.CHAR(36), db.ForeignKey("usuarios.id"), nullable=False)


class Peca(db.Model):
    __tablename__ = "pecas"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=False, default=datetime.now)
    nome = db.Column(db.String(32), nullable=False)
    pedra = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    total_peca = db.Column(db.Integer, nullable=False)
    total_pedra = db.Column(db.Integer, nullable=False)
    lucro = db.Column(db.Float, nullable=False)

    usuarios_id = db.Column(db.CHAR(36), db.ForeignKey("usuarios.id"), nullable=False)
    meses_id = db.Column(db.CHAR(36), db.ForeignKey("meses.id"), nullable=False)
