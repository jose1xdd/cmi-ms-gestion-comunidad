from sqlalchemy.orm import Session
from app.persistence.model.parcialidad import Parcialidad
from app.persistence.repository.base_repository.impl.base_repository import BaseRepository
from app.persistence.repository.parcialidad_repository.interface.interface_parcialidad_repository import IParcialiadRepository


class ParcialidadRepository(BaseRepository,IParcialiadRepository):
    def __init__(self, db: Session):
        # Llamar al constructor de la clase base
        super().__init__(Parcialidad, db)