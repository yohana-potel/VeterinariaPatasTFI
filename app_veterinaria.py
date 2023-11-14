from veterinaria import Cliente, Animal, Turno, Veterinaria

def menu():
    opcion = 0
    while opcion < 1 or opcion > 9:
        print("--")
        print("(1) Dar alta a nuevo cliente")
        print("(2) Dar de baja a cliente")
        print("(3) Modificar cliente")


        #print("(3) Dar de alta a nueva mascota")
        print("(4) Dar de baja a mascota")
        print("(5) Asignar Turno")
        print("(6) Modifcar Turno")
        print("(7) Guardar archivo")
        print("(8) Leer archivo")
        print("(9) Salir")
        
        print("--")
        opcion = int(input("Elija una opcion: "))
        print("--")
    return opcion

def run(veterinaria):
    opcion = 0
    while opcion != 9:
        opcion = menu()
        if opcion == 1:
            nombre_cliente = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("Dni: ")
            telefono = input("Telefono: ")
            dire = input("Dirección: ")
            nombre_mascota = input("Nombre de la mascota: ")
            sexo = input("Sexo de la mascota: ")
            edad = input("Edad de la mascota: ")
            raza = input("Raza de la mascota: ")
            color = input("Color de la mascota: ")

            # Crear una instancia de Mascota
            mascota = Animal(nombre_mascota, sexo, edad, raza, color)

            # Crear una instancia de Cliente
            cliente = Cliente(dni, nombre_cliente, apellido, telefono, dire)
            cliente.asignar_mascota(mascota)  # Asignar la mascota al cliente

            if veterinaria.contiene_cliente(cliente.dni):
                print("El cliente ya existe")
            else:
                veterinaria.alta_nuevo_cliente(cliente)
                print("Cliente Agregado con su mascota")

        elif opcion == 2:

            dni_cliente = input("Ingrese el DNI del cliente a dar de baja: ")
            if veterinaria.baja_cliente(dni_cliente):
                print("Cliente eliminado con éxito")
            else:
                print("No se encontró al cliente con el DNI especificado")

        elif opcion == 3:
            dni = input("Ingrese el DNI del cliente a modificar: ")
            telefono = input("Nuevo teléfono: ")
            direccion = input("Nueva dirección: ")
            if veterinaria.modificar_cliente(dni,telefono, direccion):

                print("Cliente modificado con éxito")
            else:
                print("No se encontró al cliente con el DNI especificado")









if __name__ == "__main__":
    veterinaria = Veterinaria()
    run(veterinaria)                