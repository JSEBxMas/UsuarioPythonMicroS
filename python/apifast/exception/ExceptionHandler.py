from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from controller.Controller import router
import logging

# IMPORTACIÓN CLAVE
from pydantic_core import ValidationError as PydanticCoreError

app = FastAPI()
app.include_router(router)

# Manejo de errores de validación de FastAPI
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logging.error(f"Error de validación (FastAPI): {exc}")
    return JSONResponse(
        status_code=400,
        content={
            "mensaje": "Datos inválidos en la solicitud (FastAPI)",
            "errores": jsonable_encoder(exc.errors())
        }
    )

# Manejo de errores de validación de Pydantic Core (2.x)
@app.exception_handler(PydanticCoreError)
async def pydantic_validation_exception_handler(request: Request, exc: PydanticCoreError):
    logging.error(f"Error de validación (Pydantic): {exc}")
    return JSONResponse(
        status_code=400,
        content={
            "mensaje": "Datos inválidos en la solicitud (Pydantic)",
            "errores": jsonable_encoder(exc.errors())
        }
    )
