from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import exists
from app.persistence.model.miembro_familia import MiembroFamilia
from app.persistence.model.persona import Persona
from app.persistence.repository.base_repository.impl.base_repository import BaseRepository
from app.persistence.repository.miembro_familia_repository.interface.inteface_miembro_familia import IMiembroRepository


class MiembroRepository(BaseRepository, IMiembroRepository):
    def __init__(self, db: Session):
        super().__init__(MiembroFamilia, db)
    
    def get_familia_actual(self, persona_id: str) -> Optional[MiembroFamilia]:
        return (
            self.db.query(MiembroFamilia)
            .filter(MiembroFamilia.personaId == persona_id)
            .first()
        )
    def get_lider_familia_persona(self, familia_id: int) -> Optional[Persona]:
        return (
            self.db.query(Persona)
            .join(
                MiembroFamilia,
                MiembroFamilia.personaId == Persona.id
            )
            .filter(
                MiembroFamilia.familiaId == familia_id,
                MiembroFamilia.esRepresentante.is_(True),
                MiembroFamilia.activo.is_(True)
            )
            .one_or_none()
        )
    
    def get_lider_familia(self, familia_id: int) -> Optional[MiembroFamilia]:
        return (
            self.db.query(MiembroFamilia)
            .filter(
                MiembroFamilia.familiaId == familia_id,
                MiembroFamilia.esRepresentante.is_(True),
                MiembroFamilia.activo.is_(True)
            )
            .one_or_none()
        )