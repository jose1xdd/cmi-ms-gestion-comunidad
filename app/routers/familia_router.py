from fastapi import APIRouter
from fastapi import APIRouter, Depends, Query, Request, status

from app.ioc.container import get_familia_manager
from app.models.inputs.familia_create import FamiliaCreate
from app.services.familia_manager import FamiliaManager


familia_router = APIRouter(prefix="/familias")


@familia_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create(
        data: FamiliaCreate,
        manager: FamiliaManager = Depends(get_familia_manager)):
    return manager.create(data)


@familia_router.delete("/{id_familia}", status_code=status.HTTP_200_OK)
async def delete(
        id_familia: int,
        manager: FamiliaManager = Depends(get_familia_manager)):
    return manager.delete(id_familia)
