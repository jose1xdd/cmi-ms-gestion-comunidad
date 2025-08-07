from pydantic import BaseModel

class ParcialidadOut(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True  # Permite convertir desde modelo SQLAlchemy
