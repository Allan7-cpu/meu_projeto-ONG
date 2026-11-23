from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from model.ong import Ong
from service.ong_service import ongService

ong_bp = Blueprint("ong", __name__)
service = ongService()

def _mensagem_erro(erro):
    return render_template("mensagem.html", texto=str(erro))

@ong_bp.route("/cadastrar", methods=["GET", "POST"])
@login_required
def cadastrar():
    if request.method == "POST":
        try:
            campos = {campo: request.form.get(campo, "").strip() for campo in
                      ("nome", "email", "cep", "cidade", "endereco", "numero",
                       "pix", "cnpj", "tel", "descricao")}
            nova_ong = Ong(**campos)
            service.cadastrar(nova_ong)
            return render_template("mensagem.html", texto="ONG cadastrada com sucesso!")
        except (ValueError, TypeError) as erro:
            return _mensagem_erro(erro)
    return render_template("ong_cadastro.html")

@ong_bp.route("/listar")
@login_required
def listar():
    return render_template("ong_listagem.html", ongs=service.listar())

@ong_bp.route("/pesquisar")
@login_required
def pesquisar():
    nome = request.args.get("pesquisa", "").strip()
    return render_template("ong_listagem.html", ongs=service.pesquisar(nome))

@ong_bp.route("/alterar", methods=["GET", "POST"])
@login_required
def alterar():
    if request.method == "POST":
        try:
            id_ong = int(request.form.get("id", "0"))
            campos = {campo: request.form.get(campo, "").strip() for campo in
                      ("nome", "email", "cep", "cidade", "endereco", "numero",
                       "pix", "cnpj", "tel", "descricao")}
            ong = Ong(**campos)
            ong.id = id_ong
            service.alterar(ong)
            return render_template("mensagem.html", texto="ONG alterada com sucesso!")
        except (ValueError, TypeError) as erro:
            return _mensagem_erro(erro)

    try:
        id_ong = int(request.args.get("id", "0"))
        ong = service.get_por_id(id_ong)
        if ong is None:
            return _mensagem_erro("ONG não encontrada.")
        return render_template("ong_alterar.html", ong=ong)
    except (ValueError, TypeError) as erro:
        return _mensagem_erro(erro)

@ong_bp.route("/excluir")
@login_required
def excluir():
    try:
        id_ong = int(request.args.get("id", "0"))
        service.excluir(id_ong)
        return render_template("mensagem.html", texto="ONG excluída com sucesso!")
    except (ValueError, TypeError) as erro:
        return _mensagem_erro(erro)
