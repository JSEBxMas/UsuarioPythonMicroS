#from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel
from dto.UsuarioDto import UsuarioDto
from service.ServiceUsuario import UsuarioService
from models.Usuario import Usuario

#app = FastAPI()

router = APIRouter()
servicio = UsuarioService()

# Modelo para representar un item
class Item(BaseModel):
    nombre: str
    precio: float

# Ruta GET simple
@router.get("/obtenerUsuarios")
def obtenerUsuarios():
    return {"usuarios": servicio.obtener_usuarios()}


# Ruta GET usuario por correo
@router.get("/obtenerUsuario/{correo}")
def obtenerUsuario(correo:str):
    usuario = servicio.obtener_por_correo(correo)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"usuarios": usuario}


# Ruta POST para recibir un objeto
@router.post("/agregarUsuaario")
def crear_item(item: UsuarioDto ):
    datosUsuario = Usuario(item.nombre,item.primerApellido,item.segundoApellido,item.correo,item.edad)
    servicio.crear_usuario(datosUsuario)
    return {"mensaje": "usuario creado"}



# Ruta PUT, modificar por correo
@router.put("/actualizarUsuaario")
def actualizar_item(item: UsuarioDto, correo:str ):
    datosUsuario = Usuario(item.nombre,item.primerApellido,item.segundoApellido,item.correo,item.edad)
    usuario = servicio.actualizar_usuario(correo,datosUsuario)
    return {"usuarios": usuario.modified_count}



# Ruta PUT, modificar por correo
@router.delete("/eliminarUsuaario/{correo}")
def actualizar_item(correo:str ):
    usuario = servicio.eliminar_usuario(correo)
    return {"usuarios": usuario.deleted_count}