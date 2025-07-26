from datetime import datetime
import traceback
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from app.utils.exceptions_handlers.models.error_response import AppException, ErrorResponse

def format_validation_errors(errors: list) -> str:
    mensajes = []
    for err in errors:
        loc = " -> ".join(str(e) for e in err.get("loc", []))
        msg = err.get("msg", "Error desconocido")
        input_val = err.get("input", None)

        if input_val:
            mensajes.append(f"Campo '{loc}': {msg}. Valor recibido: '{input_val}'")
        else:
            mensajes.append(f"Campo '{loc}': {msg}")
    return " | ".join(mensajes)

async def global_exception_handler(request: Request, exc: Exception):
    error = ErrorResponse(
        codigo_http=str(HTTP_500_INTERNAL_SERVER_ERROR),
        mensaje=str(exc),
        fecha=datetime.utcnow().isoformat()
    )
    
    # Si deseas imprimir el error completo en consola (stack trace):
    traceback.print_exc()

    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content=error.__dict__  # Convierte el dataclass a dict
    )
async def custom_app_exception_handler(request: Request, exc: AppException):
    error = ErrorResponse(
        codigo_http=str(exc.codigo_http),
        mensaje=exc.mensaje,
        fecha=datetime.utcnow().isoformat()
    )
    return JSONResponse(status_code=exc.codigo_http, content=error.__dict__)

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    mensaje_limpio = format_validation_errors(exc.errors())
    error = ErrorResponse(
        codigo_http=HTTP_400_BAD_REQUEST,
        mensaje=f"Error de validación: {mensaje_limpio}",
        fecha=datetime.utcnow().isoformat()
    )
    return JSONResponse(status_code=HTTP_400_BAD_REQUEST, content=error.__dict__)