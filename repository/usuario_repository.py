from database import Session
from model.usuario import Usuario
from werkzeug.security import check_password_hash

class UsuarioRepository:
    def cadastrar(self, usuario):
        session = Session()
        try:
            session.add(usuario)
            session.commit()
        finally:
            session.close()

    def login(self, username, senha):
        session = Session()
        try:
            usuario = session.query(Usuario).filter_by(username=username).first()
            if usuario and check_password_hash(usuario.password, senha):
                # O objeto permanece utilizável após o fechamento da sessão.
                session.expunge(usuario)
                return usuario
            return None
        finally:
            session.close()

    def carregar_usuario(self, id):
        session = Session()
        try:
            usuario = session.get(Usuario, int(id))
            if usuario:
                session.expunge(usuario)
            return usuario
        finally:
            session.close()
