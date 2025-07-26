from sqlalchemy.orm import Session
from app.persistence.model.familia import Familia
from app.persistence.repository.base_repository.impl.base_repository import BaseRepository
from app.persistence.repository.familia_repository.interface.interface_familia_repository import IFamiliaRepository
from app.persistence.repository.parcialidad_repository.interface.interface_parcialidad_repository import IParcialiadRepository


class FamiliaRepository(BaseRepository,IFamiliaRepository):
    def __init__(self, db: Session):
        # Llamar al constructor de la clase base
        super().__init__(Familia, db)