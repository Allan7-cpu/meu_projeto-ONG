import os
from flask import Flask
from flask_login import LoginManager
from controller.index_controller import index_bp
from controller.sobre_controller import sobre_bp
from controller.contato_controller import contato_bp
from controller.ong_controller import ong_bp
from controller.usuario_controller import usuario_bp
from database import Base, engine
from service.usuario_service import UsuarioService

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "chavesecreta-local")

app.register_blueprint(index_bp)
app.register_blueprint(sobre_bp)
app.register_blueprint(contato_bp)
app.register_blueprint(ong_bp)
app.register_blueprint(usuario_bp)

Base.metadata.create_all(engine)

login_manager = LoginManager(app)
login_manager.login_view = "usuario.login"

@login_manager.user_loader
def load_user(user_id):
    service = UsuarioService()
    return service.carregar_usuario(user_id)

if __name__ == "__main__":
    app.run(port=9000, debug=True)
