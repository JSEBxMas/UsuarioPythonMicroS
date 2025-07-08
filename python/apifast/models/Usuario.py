class Usuario():
    
    def __init__(self,nombre:str="",primerApellido:str="",segundoApellido:str="", correo:str="",edad:int=0):
        self._nombre=nombre
        self._primerApellido=primerApellido
        self._segundoApellido=segundoApellido
        self._correo=correo
        self._edad=edad
        
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre:str):
        self._nombre=nombre
        
    
    @property
    def primerApellido(self):
        return self._primerApellido

    @primerApellido.setter
    def primerApillido(self, primerApillido:str):
        self._primerApellido=primerApillido
    
    
    
    @property
    def segundoApellido(self):
        return self._segundoApellido

    @segundoApellido.setter
    def segundoApellido(self, segundoApellido:str):
        self._segundoApellido=segundoApellido
        
        
    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo:str):
        self._correo=correo
        
        
        
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad:int):
        self._edad=edad
        
        
    def to_dict(self):
        return {
            "nombre":self._nombre,
            "apellido":self._primerApellido+self._segundoApellido,
            "correo":self._correo,
            "edad": self._edad 
        }
