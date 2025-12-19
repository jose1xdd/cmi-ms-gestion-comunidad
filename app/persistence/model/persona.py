from sqlalchemy import Column, Enum, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from app.persistence.model.enum import (
    EnumDocumento, EnumEscolaridad, EnumParentesco, EnumSexo
)


class Persona(Base):
    __tablename__ = 'Persona'

    id = Column(String(255), primary_key=True)
    tipoDocumento = Column(Enum(EnumDocumento))
    nombre = Column(String(255))
    apellido = Column(String(255))
    fechaNacimiento = Column(Date)
    parentesco = Column(Enum(EnumParentesco))
    sexo = Column(Enum(EnumSexo))
    profesion = Column(String(255), nullable=True)
    escolaridad = Column(Enum(EnumEscolaridad))
    direccion = Column(String(255))
    telefono = Column(String(255))
    fechaDefuncion = Column(Date, nullable=True)

    idParcialidad = Column(
        Integer,
        ForeignKey('Parcialidad.id'),
        nullable=True
    )

    # Relaciones
    parcialidad = relationship("Parcialidad", back_populates="personas")
    usuario = relationship("Usuario", back_populates="persona", uselist=False)

    # Relación indirecta a Familia
    familias = relationship(
        "MiembroFamilia",
        back_populates="persona"
    )

    def __repr__(self):
        return "<Persona>"
