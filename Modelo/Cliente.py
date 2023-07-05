class Cliente:
    def __init__(self, apellido, nombre, dni, domicilio, telefono, email):
        self._apellido = apellido
        self._nombre = nombre
        self._dni = dni
        self._domicilio = domicilio
        self._telefono = telefono
        self._email = email
    
    def getApellido(self):
        return self._apellido
    
    def setApellido(self, apellido):
        self._apellido = apellido
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getDni(self):
        return self._dni
    
    def setDni(self, dni):
        self._dni = dni
    
    def getDomicilio(self):
        return self._domicilio
    
    def setDomicilio(self, domicilio):
        self._domicilio = domicilio
    
    def getTelefono(self):
        return self._telefono
    
    def setTelefono(self, telefono):
        self._telefono = telefono
    
    def getEmail(self):
        return self._email
    
    def setEmail(self, email):
        self._email = email
    
    def __str__(self) -> str:
        return self._apellido+", "+self._nombre
    