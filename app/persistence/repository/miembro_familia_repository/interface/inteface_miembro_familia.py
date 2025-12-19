from abc import ABC, abstractmethod
from typing import Optional
from app.persistence.model.miembro_familia import MiembroFamilia
from app.persistence.model.persona import Persona
from app.persistence.repository.base_repository.interface.ibase_repository import IBaseRepository


class IMiembroRepository(IBaseRepository[MiembroFamilia, int], ABC):
    @abstractmethod
    def get_familia_actual(self, persona_id: str) -> Optional[MiembroFamilia]:
        pass

    @abstractmethod
    def get_lider_familia_persona(self, familia_id: int) -> Optional[Persona]:
        pass

    @abstractmethod
    def get_lider_familia(self, familia_id: int) -> Optional[MiembroFamilia]:
        pass
