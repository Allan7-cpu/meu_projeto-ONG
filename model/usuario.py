from sqlalchemy import Column, Integer, String, Float
from database import Base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

class Usuario(Base, UserMixin):
    __tablename__ = "usuario"
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, username:str, password:str):
        self.username = username
        self.password = generate_password_hash(password)
    
    @property
    def is_active(self):
        return True

    @property
    def is_autenticated(self):
        return False