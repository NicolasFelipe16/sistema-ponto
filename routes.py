from flask import Blueprint, render_template, redirect, url_for, request
from models import db, usuarios

routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    return redirect(url_for('routes.login'))

@routes.route("/login")
def login():
    return render_template('index.html')

@routes.route("/enviar_dados_login", methods=['POST'])
def enviar_dados_login():
    # id = request.form("id")
    # password = request.form.get("password")

    # AINDA NÃO FAZ VALIDAÇÃO

    return redirect('/dashboard')

@routes.route("/cadastro_funcionario")
def cadastro_funcionario():
    return render_template('cadastro_funcionario.html')

@routes.route("/enviar_dados_funcionario", methods=['POST'])
def enviar_dados_funcionario():
    name = request.form.get("name")
    surname = request.form.get("surname")
    email = request.form.get("email")
    password = request.form.get("password")

    user = usuarios(
        permissao="usuario",
        nome=name,
        sobrenome=surname,
        senha=password
    )

    db.session.add(user)
    db.session.commit()

    return redirect('/dashboard')

@routes.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@routes.route("/bate-ponto")
def bate_ponto():
    return render_template('bate_ponto.html')

@routes.route("/justificativas")
def justificativas():
    return render_template('justificativas.html')

@routes.route("/registrar-justificativa")
def registrar_justificativa():
    return render_template('registra_justificativa.html')

@routes.route("/relatorio")
def relatorio():
    return render_template('relatorio.html')

@routes.route("/perfil")
def perfil():
    return render_template('perfil.html')