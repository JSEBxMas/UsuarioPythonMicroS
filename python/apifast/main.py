from fastapi import FastAPI
from controller.Controller import router as usuario_router

app = FastAPI()

app.include_router(usuario_router)
