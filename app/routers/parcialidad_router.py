
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.ioc.container import get_parcialidad_manager
from app.models.inputs.parcialidad.parcialidad_create import ParcialidadCreate
from app.models.outputs.response_estado import EstadoResponse
from app.services.parcialidad_manager import ParcialidadManager


parcialialidad_router = APIRouter(prefix="/parcialidad", tags=["Parcialidad"])


@parcialialidad_router.post("/create", status_code=status.HTTP_201_CREATED, response_model=EstadoResponse)
def create(data: ParcialidadCreate,
           manager: ParcialidadManager = Depends(get_parcialidad_manager)):
    response = manager.create(data)
    return JSONResponse(content=response.model_dump(exclude_none=True), status_code=201)


@parcialialidad_router.delete("/{id_parcialidad}", status_code=status.HTTP_200_OK, response_model=EstadoResponse)
def delete(
    id_parcialidad: int,
    manager: ParcialidadManager = Depends(get_parcialidad_manager)):
    response = manager.delete(id_parcialidad)
    return JSONResponse(content=response.model_dump(exclude_none=True), status_code=200)
