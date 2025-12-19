from datetime import date, datetime
from sqlalchemy import Column, Integer, Enum, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.config.database import Base
from app.persistence.model.enum import EnumEstadoFamilia


class Familia(Base):
    __tablename__ = 'Familia'

    id = Column(Integer, primary_key=True, autoincrement=True)

    estado = Column(
        Enum(EnumEstadoFamilia),
        default=EnumEstadoFamilia.ACTIVA,
        nullable=False
    )

    fechaCreacion = Column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now()
    )

    # Relación SOLO a través de MiembroFamilia
    miembros = relationship(
        "MiembroFamilia",
        back_populates="familia",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "estado": self.estado.value if hasattr(self.estado, "value") else self.estado,
            "fechaCreacion": (
                self.fechaCreacion.strftime("%Y-%m-%d")
                if isinstance(self.fechaCreacion, (datetime, date))
                else self.fechaCreacion
            )
        }