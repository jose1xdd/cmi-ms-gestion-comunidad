from abc import ABC, abstractmethod
from app.persistence.model.persona import Persona
from app.persistence.repository.base_repository.interface.ibase_repository import IBaseRepository


class IPersonaRepository(IBaseRepository[Persona, str], ABC):
    @abstractmethod
    def find_familia_members(self, id: int)->int:
        pass
