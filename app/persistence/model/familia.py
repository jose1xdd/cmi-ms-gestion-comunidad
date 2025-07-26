from sqlalchemy import  Column, Integer
from app.config.database import Base
from sqlalchemy.orm import relationship

class Familia(Base):
    __tablename__ = 'Familia'

    id = Column(Integer, primary_key=True, autoincrement=True)
    integrantes = Column(Integer)

    personas = relationship("Persona", back_populates="familia")