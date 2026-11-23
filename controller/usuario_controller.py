from flask import Blueprint, render_template, request
from flask_login import login_user, logout_user, login_required, current_user
from model.usuario import Usuario
from service.usuario_service import UsuarioService
from database import Session
from model.ong import Ong
from model.usuario import Usuario

usuario_bp = Blueprint("usuario", __name__)
service = UsuarioService()

@usuario_bp.route("/registrar", methods=["GET","POST"])
def registrar():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirmar_senha = request.form.get("confirmar_senha", "")
        try:
            service.cadastrar(username, email, password, confirmar_senha)
        except ValueError as erro:
            return render_template("mensagem.html", texto=str(erro))
        return render_template("login.html")
    else:
        return render_template("registrar.html")

@usuario_bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        usuario = service.login(username, password)
        if usuario:
            login_user(usuario)
            return render_template("dashboard.html", current_user=current_user)
        else:
            return render_template("mensagem.html", texto="Login inválido!")
    return render_template("login.html")

@usuario_bp.route("/dashboard")
@login_required
def dashboard():
    session = Session()
    try:
        total_ongs = session.query(Ong).count()
        total_usuarios = session.query(Usuario).count()
        ongs_recentes = (
            session.query(Ong)
            .order_by(Ong.id.desc())
            .limit(5)
            .all()
        )
    finally:
        session.close()

    return render_template(
        "dashboard.html",
        current_user=current_user,
        total_ongs=total_ongs,
        total_usuarios=total_usuarios,
        ongs_recentes=ongs_recentes
    )

@usuario_bp.route("/logout")
def logout():
    logout_user()
    return render_template("login.html")