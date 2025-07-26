from abc import ABC, abstractmethod
from typing import Optional
from app.persistence.model.usuario import Usuario
from app.persistence.repository.base_repository.interface.ibase_repository import IBaseRepository

class IUsuarioRepository(IBaseRepository[Usuario, str], ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[Usuario]:
        pass

    @abstractmethod
    def update_password(self, email: str, password: str) -> Optional[Usuario]:
        pass
