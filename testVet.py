from veterinaria import *
# from videoclub_abb import *

# --- TESTS CLASE Veterinaria ---
veterinaria = Veterinaria()

# Test crear cliente y mascota 

cliente = Cliente(33120321,"Yohana","potel",4942815,"calle 123")
veterinaria.alta_nuevo_cliente(cliente)
assert veterinaria.contiene_cliente(33120321) == True

# Test buscar cliente
test_buscar = veterinaria.buscar_cliente(33120321)
assert test_buscar.dni == 33120321
"""

# Test crear pelicula y contiene pelicula
peli = Pelicula("Jumanji","Comedia",1995)
videoclub.alta_nueva_pelicula(peli)
print(videoclub.contiene_pelicula("Jumanji"))

# Test buscar pelicula
pelicula = videoclub.buscar_pelicula("Jumanji")
assert pelicula.titulo == "Jumanji"

# Test alquilar pelicula
videoclub.alquilar_pelicula("Jumanji",30331261)
pelicula = videoclub.buscar_pelicula("Jumanji")
assert pelicula.esta_alquilada() == True

# Test devolver pelicula
videoclub.devolver_pelicula("Jumanji")
pelicula = videoclub.buscar_pelicula("Jumanji")
assert pelicula.esta_alquilada() == False

# Test baja socio
videoclub.baja_socio(30331261)
assert videoclub.contiene_socio(30331261) == False

# Test baja pelicula
videoclub.baja_pelicula("Jumanji")
assert videoclub.contiene_pelicula("Jumanji") == False

# --- TEST CLASE SOCIO ---
socio = Socio(30331261,"Matias",4804828,"Av Siempreviva 1234")
assert (socio == socio) == True
socio2 = Socio(40331261,"Natanael",3515645489,"Nueva cordoba")
assert (socio == socio2) == False
print(socio < socio2)
print(socio <= socio2)
print(socio != socio2)
print(socio > socio2)
print(socio >= socio2)


"""