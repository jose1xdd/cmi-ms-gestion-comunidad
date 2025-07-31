import logging

from app.models.inputs.familia_create import FamiliaCreate
from app.persistence.model.familia import Familia
from app.persistence.repository.familia_repository.interface.interface_familia_repository import IFamiliaRepository
from app.utils.exceptions_handlers.models.error_response import AppException


class FamiliaManager():
    def __init__(self,
                 familia_repository: IFamiliaRepository,
                 logger: logging.Logger):
        self.familia_repository = familia_repository
        self.logger = logger

    def create(self, data: FamiliaCreate):
        if not data.idFamilia:
            return self.familia_repository.create(Familia(integrantes=0))
        familia_exist = self.familia_repository.get(data.idFamilia)
        if familia_exist:
            self.logger.error(
                f"el numero de la familia a crear ya existe: {data.idFamilia}")
            raise AppException("La Familia a crear ya existe")
        return self.familia_repository.create(Familia(integrantes=0, id=data.idFamilia))

    def delete(self, familia_id: int):
        return self.familia_repository.delete(familia_id)
