from dataclasses import dataclass
from fastapi import status

@dataclass
class ErrorResponse():
    codigo_http: str
    mensaje: str
    fecha: str


class AppException(Exception):
    def __init__(self, mensaje: str, codigo_http: int = status.HTTP_400_BAD_REQUEST):
        self.mensaje = mensaje
        self.codigo_http = codigo_http
