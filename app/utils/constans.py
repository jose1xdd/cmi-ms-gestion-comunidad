from app.persistence.model.enum import EnumDocumento, EnumEscolaridad, EnumParentesco, EnumSexo


AUTH_HEADER = "Authorization"
COLUMNS_PERSONA = [
    "id",
    "tipoDocumento",
    "nombre",
    "apellido",
    "fechaNacimiento",
    "sexo",
    "profesion",
    "escolaridad",
    "direccion",
    "telefono",
    "parcialidad"
]
COLUMNS_PARCIALIDAD = ["nombre_parcialidad"]
COLUMNS_FAMILIA = ["idFamilia","cedulaRepresentante"]

VALID_DOC = {e.value for e in EnumDocumento}
VALID_SEXO = {e.value for e in EnumSexo}
VALID_PARENTESCO = {e.value for e in EnumParentesco}
VALID_ESCOLARIDAD = {e.value for e in EnumEscolaridad}