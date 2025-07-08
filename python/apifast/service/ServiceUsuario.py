from config.ConectionMongo import db
from models.Usuario import Usuario

class UsuarioService:
    def __init__(self):
        self.coleccion = db["usuario"]

    def crear_usuario(self, usuario: Usuario):
        self.coleccion.insert_one(usuario.to_dict())
        
    def obtener_usuarios(self):
        return list(self.coleccion.find({}, {"_id": 0}))

    def obtener_por_correo(self, correo: str):
        return self.coleccion.find_one({"correo": correo}, {"_id": 0})

    def actualizar_usuario(self, correo: str, usuario: Usuario):
        return self.coleccion.update_one({"correo": correo}, {"$set": usuario.to_dict()})

    def eliminar_usuario(self, correo: str):
        return self.coleccion.delete_one({"correo": correo})