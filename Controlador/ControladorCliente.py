from Modelo.Cliente import Cliente
from Vista.VistaCliente import VistaCliente


class ControladorCliente:
    def __init__(self, archivoClientes):
        self.cliente = Cliente(apellido='', nombre='', dni=0, domicilio='', telefono=0, email='')
        self.vista = VistaCliente()
        self.archivo = archivoClientes
        self.listaClientes = []
        self.opcion = 0
    
    def cargarArchivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    linea = line.strip().split(",")
                    self.cliente = Cliente(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5])
                    self.listaClientes.append(self.cliente)
        except FileNotFoundError:
            self.vista.archivoNoEncontrado()
    
    def registrarCliente(self):
        nuevoCliente = Cliente(apellido='', nombre='', dni=0, domicilio='', telefono=0, email='')
        self.vistaEvento.limpiar_pantalla()
        nuevoCliente.setApellido(self.vista.apellido())
        while nuevoCliente.getApellido().strip() == "":
            nuevoCliente.setApellido(self.vista.apellido())
        nuevoCliente.setNombre(self.vista.nombre())
        while nuevoCliente.getNombre().strip() == "":
            nuevoCliente.setNombre(self.vista.nombre())
        nuevoCliente.setDni(self.vista.dni())
        while nuevoCliente.getDni() == 0:
            nuevoCliente.setDni(self.vista.dni())
        nuevoCliente.setDomicilio(self.vista.domicilio())
        while nuevoCliente.getDomicilio().strip() == "":
            nuevoCliente.setDomicilio(self.vista.domicilio())
        nuevoCliente.setTelefono(self.vista.telefono())
        while nuevoCliente.getTelefono() == 0:
            nuevoCliente.setTelefono(self.vista.telefono())
        nuevoCliente.setEmail(self.vista.email())
        mailValido = False
        for char in nuevoCliente.getEmail():
            if char == "@":
                mailValido = True
        while nuevoCliente.getEmail().strip() == "" or mailValido == False:
            nuevoCliente.setEmail(self.vista.email())
        self.listaClientes.append(nuevoCliente)
        self.vista.registroExitoso()
        self.vistaEvento.limpiar_pantalla()
        self.vistaEvento.tiempo_espera()
    
    def consultarCliente(self):
        var1=1
        while var1<2:
            try:
                dniCliente = self.vista.dni()
                var1=3  
            except ValueError:
                self.vista.valorIncorrecto()
        
        for cliente in self.listaClientes:
            if int(cliente.getDni()) == dniCliente:
                self.vistaEvento.limpiar_pantalla()
                self.vista.clienteEncontrado()
                self.vista.mostrar(f"Cliente: {cliente.getApellido()} {cliente.getNombre()}.")
                self.vista.mostrar(f"Domicilio: {cliente.getDomicilio()}")
                self.vista.mostrar(f"Teléfono: {cliente.getTelefono()}")
                self.vista.mostrar(f"Email: {cliente.getEmail()}")
                self.vista.mostrar(f"{'-':-^46}")
                self.cliente = cliente
                return True
        self.vistaEvento.limpiar_pantalla()
        self.vista.clienteNoEncontrado()
        return False
    
    def modificarCliente(self):
        var1=1
        while var1<2:
            try:
                dniCliente = self.vista.dni()
                var1=3  
            
                for cliente in self.listaClientes:
                    if int(cliente.getDni()) == dniCliente:
                        opcion = 0
                        while opcion != 7:
                            opcion = self.vista.menuModificarCliente()
                            while opcion < 1 or opcion > 7:
                                opcion = self.vista.menuModificarCliente()
                            if opcion == 1:
                                cliente.setApellido(self.vista.apellido())
                            elif opcion == 2:
                                cliente.setNombre(self.vista.nombre())
                            elif opcion == 3:
                                cliente.setDni(self.vista.dni())
                            elif opcion == 4:
                                cliente.setDomicilio(self.vista.domicilio())
                            elif opcion == 5:
                                cliente.setTelefono(self.vista.telefono())
                            elif opcion == 6:
                                cliente.setEmail(self.vista.email())
                            elif opcion == 7:
                                self.guardarArchivo()
                                self.vista.registroExitoso()
            except ValueError:
                self.vista.valorIncorrecto()

    def guardarArchivo(self):
        with open(self.archivo, "w", encoding="utf-8") as archivo:
            for cliente in self.listaClientes:
                archivo.write(str(cliente.getApellido()) + "," + str(cliente.getNombre()) + "," + str(cliente.getDni()) + "," + str(cliente.getDomicilio()) + "," + str(cliente.getTelefono()) + "," + str(cliente.getEmail()) + "\n")