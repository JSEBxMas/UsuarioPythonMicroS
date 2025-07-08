from pydantic import BaseModel, EmailStr, Field 

class UsuarioDto(BaseModel):
    nombre:str 
    primerApellido:str
    segundoApellido:str
    correo: EmailStr
    edad : int = Field(...,ge=1)
        