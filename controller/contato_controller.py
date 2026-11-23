from flask import Blueprint, render_template, request

contato_bp = Blueprint("contato", __name__)

@contato_bp.route("/contato", methods=["GET", "POST"])
def contato():
    dados = ""
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        mensagem = request.form.get("mensagem", "").strip()
        if nome and email and mensagem:
            dados = "Mensagem recebida. Obrigado pelo contato!"
        else:
            dados = "Preencha todos os campos antes de enviar."
    return render_template("contato.html", dados=dados)
