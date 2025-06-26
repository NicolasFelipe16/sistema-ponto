from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    permissao = db.Column(db.String(20), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    sobrenome = db.Column(db.String(50), nullable=True)
    senha = db.Column(db.Integer, nullable=False)

class pontos(db.Model):
    __tablename__ = 'pontos'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, ForeignKey('usuarios.id'), nullable=False)
    data = db.Column(db.Date, default=datetime.date.today)
    horario = db.Column(db.Time, default=datetime.datetime.now().time)
    justificativa = db.Column(db.String, nullable=True)
    tipo = db.Column(db.String(10), nullable=False)