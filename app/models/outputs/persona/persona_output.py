from pydantic import BaseModel
from typing import Optional
from datetime import date
from app.models.outputs.parcialidad.parcialidad_output import ParcialidadOut
from app.persistence.model.enum import EnumDocumento, EnumEscolaridad, EnumParentesco, EnumSexo


class PersonaOut(BaseModel):
    id: str
    tipoDocumento: EnumDocumento
    nombre: str
    apellido: str
    fechaNacimiento: date
    parentesco: EnumParentesco
    sexo: EnumSexo
    profesion: Optional[str]
    escolaridad: EnumEscolaridad
    direccion: str
    telefono: str
    activo: bool
    idFamilia: Optional[int]
    parcialidad: Optional[ParcialidadOut]

    class Config:
        from_attributes = True
        exclude_none = True
