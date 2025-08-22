class Cliente: # Clase de entidad - clase de dominio
    def __init__(self, id_cliente=None, nombre_cliente=None, apellido_cliente=None, membrecia_cliente=None): # None: para que sea opcional pasar cualquier parametro 
        self._id_cliente = id_cliente
        self._nombre_cliente = nombre_cliente
        self._apellido_cliente = apellido_cliente
        self._membrecia_cliente = membrecia_cliente
    
    def __str__(self):
        return (f'id: {self.id_cliente}, Nombre: {self.nombre_cliente}, Apellido: {self._apellido_cliente}, Membrecia: {self._membrecia_cliente}')

    @property
    def id_cliente(self):
        return self._id_cliente
    
    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    @property
    def nombre_cliente(self):
        return self._nombre_cliente
    
    @nombre_cliente.setter
    def nombre_cliente(self, nombre_cliente):
        self
    @property
    def apellido_cliente(self):
        return self._apellido_cliente
    
    @apellido_cliente.setter
    def apellido_cliente(self, apellido_cliente):
        self._apellido_cliente = apellido_cliente

    @property
    def membrecia_cliente(self):
        return self._membrecia_cliente
    
    @membrecia_cliente.setter
    def membrecia_cliente(self, membrecia_cliente):
        self._membrecia_cliente = membrecia_cliente