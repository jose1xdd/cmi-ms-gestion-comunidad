from sqlalchemy import  Column, String, Integer
from app.config.database import Base
from sqlalchemy.orm import relationship

class Parcialidad(Base):
    __tablename__ = 'Parcialidad'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))  # Puedes ajustar el tamaño si lo sabes

    personas = relationship("Persona", back_populates="parcialidad")