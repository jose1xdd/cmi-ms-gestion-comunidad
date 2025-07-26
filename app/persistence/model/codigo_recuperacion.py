from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base


class CodigoRecuperacion(Base):
    __tablename__ = "CodigoRecuperacion"

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(20), nullable=False)
    estado = Column(Boolean, default=True, nullable=False)

    emailUsuario = Column(String(100), ForeignKey(
        "Usuario.email"), nullable=False)
    usuario = relationship("Usuario", back_populates="codigos")

    def to_dict(self):
        return {
            "id": self.id,
            "codigo": self.codigo,
            "estado": self.estado,
            "emailUsuario": self.emailUsuario
        }
