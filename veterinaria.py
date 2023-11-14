import pickle #libreria para guardar y recuperar informacion



class Cliente():
    def __init__(self, dni, nombre, apellido, telefono, direccion):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.mascotas = []

    def asignar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def __lt__(self, other):  # x<y llama x.__lt__(y)
        return self.dni < other.dni

    def __le__(self, other):  # x<=y llama x.__le__(y)
        return self.dni <= other.dni

    def __eq__(self, other):  # x==y llama x.__eq__(y)
        return self.dni == other.dni

    def __ne__(self, other):  # x!=y llama x.__ne__(y)
        return self.dni != other.dni

    def __gt__(self, other):  # x>y llama x.__gt__(y)
        return self.dni > other.dni

    def __ge__(self, other):  # x>=y llama x.__ge__(y)
        return self.dni >= other.dni

    def __str__(self):
        mascotas_str = '\n'.join([m.nombre_mascota for m in self.mascotas])
        return f"DNI: {self.dni}\nNombre: {self.nombre}\nApellido: {self.apellido}\nTelefono: {self.telefono}\nDomicilio: {self.direccion}\nMascotas: {mascotas_str}\n"


class Animal():
    def __init__(self, nombre_mascota, sexo, edad, raza, color):
        self.nombre_mascota = nombre_mascota
        self.sexo = sexo
        self.edad = edad
        self.raza = raza
        self.color = color


class Turno():
    def __init__(self, cliente, fecha, hora, motivo_consulta):
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora
        self.motivo_consulta = motivo_consulta


class Veterinaria():
    def __init__(self):
        self.clientes = []
        self.turnos = []
        self.animales = []

    # metodo cliente

    def contiene_cliente(self, dni) -> bool:
        for cliente in self.clientes:
            if cliente.dni == dni:
                return True
        return False

    def buscar_cliente(self, dni) -> Cliente:
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        return None
    

    def alta_nuevo_cliente(self, cliente):
        if not self.contiene_cliente(cliente.dni):
            self.clientes.append(cliente)

    def baja_cliente(self, dni):
        cliente = self.buscar_cliente(dni)
        if cliente:
            self.clientes.remove(cliente)

    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def modificar_cliente(self, dni,telefono,direccion):
        cliente = self.buscar_cliente(dni)
        if cliente:
            cliente.telefono = telefono
            cliente.direccion = direccion

    # metodo de mascota

    def alta_mascota(self, mascota: Animal, dni_cliente):
        cliente = self.buscar_cliente(dni_cliente)
        if cliente:
            cliente.asignar_mascota(mascota)

    def buscar_mascota(self, dni_cliente, nombre_mascota) -> Animal:
        cliente = self.buscar_cliente(dni_cliente)
        if cliente:
            for mascota in cliente.mascotas:
                if mascota.nombre_mascota == nombre_mascota:
                    return mascota
        return None

    def baja_mascota(self, dni_cliente, nombre_mascota):
        mascota = self.buscar_mascota(dni_cliente, nombre_mascota)
        if mascota:
            cliente = self.buscar_cliente(dni_cliente)
            if cliente:
                cliente.mascotas.remove(mascota)

    def modificar_mascota(self, dni_cliente, nombre_mascota, nva_descripcion):
        mascota = self.buscar_mascota(dni_cliente, nombre_mascota)
        if mascota:
            mascota.descripcion = nva_descripcion
            print("Mascota modificada con éxito.")
        else:
            print("La mascota no fue encontrada.")

    # metodos turnos

    def nvo_turno(self, dni_cliente, fecha, hora, motivo_consulta):
        cliente = self.buscar_cliente(dni_cliente)
        if cliente:
            turno = Turno(cliente=cliente, fecha=fecha, hora=hora, motivo_consulta=motivo_consulta)
            self.turnos.append(turno)

    def eliminar_turno(self, dni_cliente, fecha, hora):
        turno = None
        for t in self.turnos:
            if t.cliente.dni == dni_cliente and t.fecha == fecha and t.hora == hora:
                turno = t
                break
        if turno:
            self.turnos.remove(turno)

    def modificar_turno(self):
        pass

    


#guardar datos 
    def guardar_archivo(self,archivo="video.pickle"):
        pickle_file = open(archivo, 'wb')
        pickle.dump(self, pickle_file)
        pickle_file.close()

    def leer_archivo(self,archivo="video.pickle"):
        pickle_file = open(archivo,'rb')
        video = pickle.load(pickle_file)
        self.cliente = video.clientes
        self.animal = video.animales
        self.turno = video.turnos
        pickle_file.close()



