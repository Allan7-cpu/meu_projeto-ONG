from flask import Blueprint, render_template

sobre_bp = Blueprint("sobre", __name__)

@sobre_bp.route("/sobre")
def sobre():
    projeto = "Projeto de Receitas."
    exibir = True
    lista = ["HTML","CSS","Python"]
    usuario = {"codigo":1, "nome":"Mariana", "email":"mariana@site.com.br"}
    return render_template("sobre.html", projeto=projeto, exibir=exibir, lista=lista, usuario=usuario)