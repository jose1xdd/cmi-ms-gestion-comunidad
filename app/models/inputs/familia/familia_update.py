from typing import Optional
from pydantic import BaseModel


class FamiliaUpdate(BaseModel):
    familiaId: int
    representanteId: Optional[str]

    class Config:
        from_attributes = True
        exclude_none = True
