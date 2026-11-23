from repository.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.__repository = UsuarioRepository()

    def cadastrar(self, usuario):
        if usuario.username == "" or usuario.password == "":
            raise ValueError("Informe o usuário e a senha!")
        self.__repository.cadastrar(usuario)
    
    def login(self, username, password):
        return self.__repository.login(username, password)

    def carregar_usuario(self, id):
        return self.__repository.carregar_usuario(id)