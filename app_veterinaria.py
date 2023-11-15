from veterinaria import Cliente, Animal, Turno, Veterinaria

def menu():
    opcion = 0
    while opcion < 1 or opcion > 9:
        print("--")
        print("(1) Dar alta a nuevo cliente")
        print("(2) Dar de baja a cliente")
        print("(3) Modificar cliente")
        print("(4) Dar de baja a mascota")
        print("(5) Asignar Turno")
        print("(6) Eliminar Turno")
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
            if veterinaria.contiene_cliente != None:
                veterinaria.baja_cliente(dni_cliente)
                print("Cliente eliminado con éxito")
            else:
                print("No se encontró al cliente con el DNI especificado")

        elif opcion == 3:
            dni = input("Ingrese el DNI del cliente a modificar: ")
            telefono = input("Nuevo teléfono: ")
            direccion = input("Nueva dirección: ")
            if veterinaria.contiene_cliente != None:
                veterinaria.modificar_cliente(dni,telefono, direccion)
                print("Cliente modificado con éxito")
            else:
                print("No se encontró al cliente con el DNI especificado")

        elif opcion == 4:
           
            dni_cliente = input("DNI del cliente: ")
            cliente = veterinaria.buscar_cliente(dni_cliente)

            if cliente != None:
                nombre_mascota = input("Nombre de la mascota a dar de baja: ")
                mascota_a_eliminar = None
                i=0
                for mascota in cliente.mascota:
                    if mascota.nombre_mascota == nombre_mascota:
                        mascota_a_eliminar = mascota
                        i+=1
                        break

                if veterinaria.baja != None:
                    cliente.mascota.remove(i)
                    veterinaria.baja_mascota(mascota_a_eliminar)
                    print("Mascota dada de baja con éxito.")
                else:
                    print("Mascota no encontrada.")
            else:
                print("Cliente no encontrado")
        
        elif opcion == 5:
            dni = input("Ingrese DNI del cliente: ")
            fecha = input("Ingrese una fecha par su turno: ")
            hora = input("Ingrese una hora par su turno: ")
            motivo_consulta = input("Ingrese motivo de Turno: ")

            nuevo_turno = Turno(dni, fecha, hora, motivo_consulta)
            

            if veterinaria.tiene_turno (nuevo_turno.dni):
                print("El cliente ya tien turno")
            else:
                veterinaria.nuevo_turno(nuevo_turno)
                print("Se genero su turno,correctamente")

        elif opcion == 6:
            dni = input("Ingrese DNI del cliente para  modificar su turno: ")
            fecha = input("NFecha a modificar: ")
            hora = input("Hora de su turno: ")
            if veterinaria.modificar_turno(dni,fecha,hora):

                print("Turno modificado con éxito")
            else:
                print("No se encontró turno para el DNI especificado")

        
            

        elif opcion == 7: #guardar archivo
            veterinaria.guardar_archivo()
            print("Datos guardados en el archivo")


        elif opcion == 8: #guardar archivo
            veterinaria.leer_archivo()
            print("Datos leídos desde el archivo")



if __name__ == "__main__":
    veterinaria = Veterinaria()
    run(veterinaria)                