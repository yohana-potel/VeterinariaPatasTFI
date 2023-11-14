import pickle  # libreria para guardar y recuperar informacion

from arbolbb import ArbolBinarioBusqueda

class Cliente():
    def __init__(self, dni, nombre, apellido, telefono, direccion):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.mascota = None
    
    def asignar_mascota(self, mascota):
        self.mascota = mascota
        
    def __lt__(self, other): # x<y llama x.__lt__(y)
        return self.dni < other.dni
    
    def __le__(self, other): # x<=y llama x.__le__(y)
        return self.dni <= other.dni
    
    def __eq__(self, other): # x==y llama x.__eq__(y)
        return self.dni == other.dni
    
    def __ne__(self, other): # x!=y llama x.__ne__(y)
        return self.dni != other.dni
    
    def __gt__(self, other): # x>y llama x.__gt__(y)
        return self.dni > other.dni
    
    def __ge__(self, other): # x>=y llama x.__ge__(y)
        return self.dni >= other.dni
    
    def __str__(self):
        return "DNI: {0}\nNombre: {1}\nApellido: {2}\nTelefono: {3}\nDomicilio: {4}\nMascota: {5}\n" \
            .format(self.dni, self.nombre, self.apellido, self.telefono, self.direccion, self.mascota)


class Animal():
    def __init__(self, nombre_mascota, sexo, edad, raza, color):
        self.nombre_mascota = nombre_mascota
        self.sexo = sexo
        self.edad = edad
        self.raza = raza
        self.color = color


class Turno():
    def __init__(self, nombre_cliente, fecha, hora, motivo_consulta):
        self.nombre_cliente = nombre_cliente
        self.fecha = fecha
        self.hora = hora
        self.motivo_consulta = motivo_consulta
    
    def __str__(self):
        return "Nombre: {0}\nFecha: {1}\nHora: {2}\nMotivo: {3}" \
            .format(self.nombre_cliente, self.fecha, self.hora, self.motivo_consulta)


class Veterinaria():
    def __init__(self):
        self.clientes = ArbolBinarioBusqueda()
        self.turnos = ArbolBinarioBusqueda()
        self.animales = ArbolBinarioBusqueda()

    def contiene_cliente(self, dni) -> bool:
        return dni in self.clientes
        
    def buscar_cliente(self, dni):
        if dni in self.clientes:
            return self.clientes[dni]

    def alta_nuevo_cliente(self, cliente):
        self.clientes[cliente.dni] = cliente
        
    def baja_cliente(self, dni):
        if dni in self.clientes:
            del self.clientes[dni]

    def modificar_cliente(self, dni, telefono, direccion):
        # Buscar el cliente por su DNI
        for cliente in self.clientes:
            if cliente.dni == dni:
                # Actualizar los datos del cliente
                cliente.telefono = telefono
                cliente.direccion = direccion
                return True  # Cliente modificado con éxito
        
        return False  # No se encontró al cliente con el DNI especificado")

    def mostrar_clientes(self):
        for cliente in self.clientes.values():
            print(cliente)
    
    # Métodos para mascotas
    def alta_mascota(self, mascota):
        self.mascotas[mascota]

    def baja_mascota(self, dni_cliente, nombre):
        del self.mascotas[nombre]
    
    def modificar_mascota(self, descripcion):
        pass
    
    
    """# Métodos para turnos
    def nuevo_turno(self, nombre_cliente, dni, fecha, hora, motivo_consulta):
        turno = Turno(nombre_cliente, fecha, hora, motivo_consulta)
        self.turnos.append(turno)

    def eliminar_turno(self, dni, fecha, hora):
        turno = next((t for t in self.turnos if t.nombre_cliente == nombre_cliente and t.fecha == fecha and t.hora == hora), None)
        if turno:
            self.turnos.remove(turno)

    def modificar_turno(self):
        pass"""

#guradar 
    def guardar_archivo(self,archivo="veterinaria.pickle"):
        pickle_file = open(archivo, 'wb')
        pickle.dump(self, pickle_file)
        pickle_file.close()

    def leer_archivo(self,archivo="veterianria.pickle"):
        pickle_file = open(archivo,'rb')
        video = pickle.load(pickle_file)
        self.clientes = video.clientes
        self.mascotas = video.animales
        self.turnos = video.turnos
        pickle_file.close()
