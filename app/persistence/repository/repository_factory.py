from typing import Type, TypeVar
from sqlalchemy.orm import Session
from app.persistence.repository.familia_repository.impl.familia_repository import FamiliaRepository
from app.persistence.repository.familia_repository.interface.interface_familia_repository import IFamiliaRepository
from app.persistence.repository.miembro_familia_repository.impl.miembro_familia_repository import MiembroRepository
from app.persistence.repository.miembro_familia_repository.interface.inteface_miembro_familia import IMiembroRepository
from app.persistence.repository.parcialidad_repository.impl.parcialidad_repository import ParcialidadRepository
from app.persistence.repository.parcialidad_repository.interface.interface_parcialidad_repository import IParcialiadRepository
from app.persistence.repository.persona_repository.impl.persona_repository import PersonaRepository
from app.persistence.repository.persona_repository.interface.interface_persona_repository import IPersonaRepository
from app.persistence.repository.user_repository.impl.user_repository import UsuarioRepository
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository

T = TypeVar("T")


class RepositoryFactory:

    def __init__(self, db: Session):
        self.db = db

    _registry: dict[Type, Type] = {
        IUsuarioRepository: UsuarioRepository,
        IPersonaRepository: PersonaRepository,
        IFamiliaRepository: FamiliaRepository,
        IParcialiadRepository: ParcialidadRepository,
        IMiembroRepository: MiembroRepository
    }

    def get_repository(self, interface: Type[T]) -> T:
        impl_class = self._registry.get(interface)
        if not impl_class:
            raise ValueError(
                f"No hay implementación registrada para la interfaz: {interface}")
        # Solo pasamos db, el modelo se define en el repositorio
        return impl_class(self.db)
