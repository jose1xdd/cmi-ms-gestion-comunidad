from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from app.config.database import Base


class MiembroFamilia(Base):
    __tablename__ = 'MiembroFamilia'

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    personaId = Column(
        String(255),
        ForeignKey('Persona.id', ondelete="CASCADE"),
        nullable=False
    )

    familiaId = Column(
        Integer,
        ForeignKey('Familia.id', ondelete="CASCADE"),
        nullable=False
    )

    activo = Column(Boolean, nullable=False, default=True)

    esRepresentante = Column(Boolean, nullable=False, default=False)

    # Relaciones
    persona = relationship(
        "Persona",
        back_populates="familias"
    )

    familia = relationship(
        "Familia",
        back_populates="miembros"
    )

    def __repr__(self):
        return (
            f"<MiembroFamilia("
            f"personaId={self.personaId}, "
            f"familiaId={self.familiaId}, "
            f"activo={self.activo}, "
            f"esRepresentante={self.esRepresentante})>"
        )
