import logging

from app.models.inputs.persona_input import PersonaInput
from app.persistence.model.familia import Familia
from app.persistence.model.parcialidad import Parcialidad
from app.persistence.repository.familia_repository.interface.interface_familia_repository import IFamiliaRepository
from app.persistence.repository.parcialidad_repository.interface.interface_parcialidad_repository import IParcialiadRepository
from app.persistence.repository.persona_repository.interface.interface_persona_repository import IPersonaRepository
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository
from app.utils.exceptions_handlers.models.error_response import AppException
from fastapi import status


class Manager():
    def __init__(self,
                 usuario_repository: IUsuarioRepository,
                 persona_repository: IPersonaRepository,
                 familia_repository: IFamiliaRepository,
                 parcialidad_repository: IParcialiadRepository,
                 logger: logging.Logger):
        self.usuario_repository = usuario_repository
        self.logger = logger
        self.persona_repository = persona_repository
        self.familia_repository = familia_repository
        self.parcialidad_repository = parcialidad_repository

    def create_person(self, data: PersonaInput):
        # Validar existencia de la familia
        familia: Familia = self.familia_repository.get(data.idFamilia)
        if not familia:
            raise AppException("La Familia asignada no existe")

        # Validar límite de miembros
        miembros_actuales = self.persona_repository.find_familia_members(data.idFamilia)
        if miembros_actuales >= familia.integrantes:
            raise AppException("Cantidad máxima de miembros alcanzada")

        # Validar existencia de la parcialidad
        if not self.parcialidad_repository.get(data.idParcialidad):
            raise AppException("Parcialidad no existente")

        # Validar si la persona ya existe
        if self.persona_repository.get(data.id):
            raise AppException("Ese documento ya se encuentra registrado")

        # Crear la persona
        self.persona_repository.create(data)
