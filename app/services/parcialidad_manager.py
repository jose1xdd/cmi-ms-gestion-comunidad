
import logging

from app.models.inputs.parcialidad.parcialidad_create import ParcialidadCreate
from app.models.outputs.response_estado import EstadoResponse
from app.persistence.model.parcialidad import Parcialidad
from app.persistence.repository.parcialidad_repository.interface.interface_parcialidad_repository import IParcialiadRepository
from app.utils.exceptions_handlers.models.error_response import AppException


class ParcialidadManager():

    def __init__(self,
                 parcialidad_repository: IParcialiadRepository,
                 logger: logging.Logger):
        self.parcialidad_repository: IParcialiadRepository = parcialidad_repository
        self.logger: logging.Logger = logger

    def create(self, data: ParcialidadCreate):
        parcialidad = self.parcialidad_repository.find_by_name(
            data.nombre_parcialidad)
        if parcialidad is not None:
            raise AppException("ya existe una parcialidad con ese nombre")
        self.parcialidad_repository.create(
            Parcialidad(nombre=data.nombre_parcialidad))
        return EstadoResponse(estado="Exitoso",
                              message="Parcialidad creada exitosamente")

    def delete(self, parcialidad_id: int):
        parcialidad = self.parcialidad_repository.get(parcialidad_id)
        if parcialidad is None:
            raise AppException(
                f"No existe una parcialidad con ese id : {parcialidad_id}")
        self.parcialidad_repository.delete(parcialidad.id)
        return EstadoResponse(estado="Exitoso",
                              message="Parcialidad eliminada exitosamente")
