from abc import ABC
from app.persistence.model.familia import Familia
from app.persistence.repository.base_repository.interface.ibase_repository import IBaseRepository


class IFamiliaRepository(IBaseRepository[Familia, int], ABC):
    pass
