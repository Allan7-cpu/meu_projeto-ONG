from database import Base
from sqlalchemy import Column, Integer, String, Float

class Ong(Base):
    __tablename__ = "Ong"
    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(250), nullable=False)
    cep = Column(String, nullable=False) 
    cidade = Column(String, nullable=False) 
    endereco = Column(String, nullable=False) 
    numero = Column(String, nullable=False) 
    pix = Column(String, nullable=False) 
    cnpj = Column(String, nullable=False) 
    tel = Column(String, nullable=False) 
    descricao = Column(String, nullable=False) 

    def __init__(self, nome:str, email:str, cep:str, cidade:str, endereco:str, numero:str, pix:str, cnpj:str, tel:str, descricao:str):
        self.nome = nome
        self.email = email
        self.cep = cep
        self.cidade = cidade
        self.endereco = endereco
        self.numero = numero
        self.pix = pix
        self.cnpj = cnpj
        self.tel = tel
        self.descricao = descricao
        