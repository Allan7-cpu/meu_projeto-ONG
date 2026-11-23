from repository.ong_repository import ongRepository

class ongService:
    def __init__(self):
        self.__repository = ongRepository()

    def _validar(self, ong):
        ong.nome = (ong.nome or "").strip()
        ong.descricao = (ong.descricao or "").strip()
        if not ong.nome:
            raise ValueError("O nome não foi preenchido.")
        if len(ong.nome) > 100:
            raise ValueError("O nome deve ter até 100 caracteres.")
        if not ong.descricao:
            raise ValueError("A descrição não foi preenchida.")
        if len(ong.descricao) > 250:
            raise ValueError("A descrição deve ter até 250 caracteres.")

    def cadastrar(self, ong):
        self._validar(ong)
        self.__repository.cadastrar(ong)

    def listar(self):
        return self.__repository.listar()

    def pesquisar(self, nome):
        return self.__repository.pesquisar(nome)

    def get_por_id(self, id):
        if id is None or int(id) <= 0:
            raise ValueError("O id deve ser maior que 0.")
        return self.__repository.get_por_id(int(id))

    def alterar(self, ong):
        self._validar(ong)
        if ong.id is None or int(ong.id) <= 0:
            raise ValueError("O id não foi informado corretamente.")
        if not self.__repository.alterar(ong):
            raise ValueError("ONG não encontrada.")

    def excluir(self, id):
        if id is None or int(id) <= 0:
            raise ValueError("O id não foi informado corretamente.")
        if not self.__repository.excluir(int(id)):
            raise ValueError("ONG não encontrada.")
