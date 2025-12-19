from typing import Any, Dict, List
from sqlalchemy import and_
from sqlalchemy.orm import Session, joinedload
from app.models.inputs.persona.persona_create import PersonaCreate
from app.models.outputs.persona.persona_output import PersonaOut
from app.persistence.model.miembro_familia import MiembroFamilia
from app.persistence.model.parcialidad import Parcialidad
from app.persistence.model.persona import Persona
from app.persistence.repository.base_repository.impl.base_repository import BaseRepository
from app.persistence.repository.persona_repository.interface.interface_persona_repository import IPersonaRepository


class PersonaRepository(BaseRepository, IPersonaRepository):
    def __init__(self, db: Session):
        super().__init__(Persona, db)

    def find_familia_members(self, id_familia: int) -> int:
        return (
            self.db.query(Persona)
            .filter(Persona.idFamilia == id_familia)
            .count()
        )

    def find_all_personas(self, page: int, page_size: int, filters: Dict[str, Any]):

        id_familia = filters.pop("idFamilia", None)

        query = self.apply_filters(self.db, Persona, filters)

        if id_familia:
            query = query.join(
                MiembroFamilia,
                and_(
                    MiembroFamilia.personaId == Persona.id,
                    MiembroFamilia.familiaId == id_familia,
                    MiembroFamilia.activo == True
                )
            )
        else:
            query = query.outerjoin(
                MiembroFamilia,
                and_(
                    MiembroFamilia.personaId == Persona.id,
                    MiembroFamilia.activo == True
                )
            )

        query = (
            query
            .outerjoin(Persona.parcialidad)
            .options(joinedload(Persona.parcialidad))
            .add_columns(MiembroFamilia.familiaId.label("idFamilia"))
        )

        page_data = self.paginate(page, page_size, query)

        personas = []
        for persona, idFamilia in page_data["items"]:
            persona.idFamilia = idFamilia
            personas.append(persona)

        page_data["items"] = personas
        return page_data

    def find_persona_by_id(self, persona_id: str):

        query = (
            self.db.query(Persona)
            .join(
                MiembroFamilia,
                and_(
                    MiembroFamilia.personaId == Persona.id,
                    MiembroFamilia.activo == True
                ),
                isouter=True
            )
            .outerjoin(Persona.parcialidad)
            .options(joinedload(Persona.parcialidad))
            .add_columns(MiembroFamilia.familiaId.label("idFamilia"))
            .filter(Persona.id == persona_id)
        )

        result = query.first()

        if not result:
            return None

        persona, idFamilia = result

        persona.idFamilia = idFamilia

        return persona

    def bulk_insert(self, personas: List[PersonaCreate]) -> int:
        for persona in personas:
            self.create(persona)
        return len(personas)

    def bulk_insert_fast(self, lista_diccionarios):
        # Crear nueva sesión aislada para el thread

        try:
            self.db.bulk_insert_mappings(Persona, lista_diccionarios)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        finally:
            self.db.close()
