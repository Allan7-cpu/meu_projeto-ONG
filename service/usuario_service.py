import re
from model.usuario import Usuario
from repository.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.__repository = UsuarioRepository()

    def cadastrar(self, username, email, password, confirmar_senha):
        if not username or not email or not password:
            raise ValueError("Informe o usuário, o e-mail e a senha!")
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            raise ValueError("Informe um e-mail válido!")
        if password != confirmar_senha:
            raise ValueError("As senhas não conferem!")
        if self.__repository.existe(username, email):
            raise ValueError("Usuário ou e-mail já cadastrado!")
        usuario = Usuario(username, email, password)
        self.__repository.cadastrar(usuario)

    def login(self, username, password):
        return self.__repository.login(username, password)

    def carregar_usuario(self, id):
        return self.__repository.carregar_usuario(id)