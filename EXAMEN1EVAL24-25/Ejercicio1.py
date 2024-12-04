#DANIEL DIAZ

from funciones.funcion1 import funcion1a,funcion1b

from funciones.funcion2 import funcion2a,funcion2bMostrar

from funciones.funcion3 import funcion3


print("EJERCICIO1\n")
#1A
personas=funcion1a("EXAMEN1EVAL24-25/assets/sitios_empleados.csv")

#1B
print("APARTADO 2")
funcion1b(personas)

print("\n\n")

print("EJERCICIO2\n")
#2A
sitios=funcion2a("EXAMEN1EVAL24-25/assets/sitios_trabajo.txt")
#2B
print("APARTADO 2")
funcion2bMostrar(personas,sitios)

print("\n\n")

print("EJERCICIO3\n")
ejercicio3=funcion3("EXAMEN1EVAL24-25/assets/sitios_empleados.csv",sitios)



                        