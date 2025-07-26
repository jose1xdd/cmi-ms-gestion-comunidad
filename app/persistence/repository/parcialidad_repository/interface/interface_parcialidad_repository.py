from abc import ABC
from app.persistence.model.parcialidad import Parcialidad
from app.persistence.repository.base_repository.interface.ibase_repository import IBaseRepository

class IParcialiadRepository(IBaseRepository[Parcialidad, int], ABC):
    pass