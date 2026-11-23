from database import Session
from model.ong import Ong

class ongRepository:
    def cadastrar(self, ong):
        session = Session()
        try:
            session.add(ong)
            session.commit()
        finally:
            session.close()

    def listar(self):
        session = Session()
        try:
            return session.query(Ong).all()
        finally:
            session.close()

    def pesquisar(self, nome):
        session = Session()
        try:
            consulta = session.query(Ong)
            if nome:
                consulta = consulta.filter(Ong.nome.like(f"%{nome}%"))
            return consulta.all()
        finally:
            session.close()

    def get_por_id(self, id):
        session = Session()
        try:
            return session.get(Ong, id)
        finally:
            session.close()

    def alterar(self, ong):
        session = Session()
        try:
            ong_anterior = session.get(Ong, ong.id)
            if ong_anterior:
                ong_anterior.nome = ong.nome
                ong_anterior.email = ong.email
                ong_anterior.tel = ong.tel
                ong_anterior.cep = ong.cep
                ong_anterior.cidade = ong.cidade
                ong_anterior.endereco = ong.endereco
                ong_anterior.numero = ong.numero
                ong_anterior.cnpj = ong.cnpj
                ong_anterior.pix = ong.pix
                ong_anterior.descricao = ong.descricao
                session.commit()
                session.refresh(ong_anterior)
                return True
            return False
        finally:
            session.close()

    def excluir(self, id):
        session = Session()
        try:
            ong = session.get(Ong, id)
            if ong:
                session.delete(ong)
                session.commit()
                return True
            return False
        finally:
            session.close()
