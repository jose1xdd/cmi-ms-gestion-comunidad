from abc import ABC, abstractmethod
from app.persistence.model.parcialidad import Parcialidad
from app.persistence.repository.base_repository.interface.ibase_repository import IBaseRepository

class IParcialiadRepository(IBaseRepository[Parcialidad, int], ABC):
    
    @abstractmethod
    def find_by_name(self,name:str)->Parcialidad:
        pass