from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.models.inputs.persona_input import PersonaInput
from app.services.manager import Manager
from app.ioc.container import Container

main_router = APIRouter()


@main_router.post("/personas/create", status_code=status.HTTP_202_ACCEPTED)
@inject
async def login(
        data: PersonaInput,
        manager: Manager = Depends(Provide[Container.manager])):
    manager.create_person(data)
    return {}
