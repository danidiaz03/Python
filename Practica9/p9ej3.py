# contador.py
import sys,os

def gestionar_contador(accion):
    fichero = "contador.txt"
    
    # Leer o inicializar el contador
    if not os.path.exists(fichero):
        contador = 0
    else:
        with open(fichero, "r") as f:
            contenido = f.read()
            contador = int(contenido) if contenido else 0
    
    # Modificar el contador según la acción
    if accion == "inc":
        contador += 1
    elif accion == "dec":
        contador -= 1
    
    # Mostrar el contador
    print(f"Contador: {contador}")
    
    # Guardar el nuevo valor
    with open(fichero, "w") as f:
        f.write(str(contador))

if __name__ == "__main__":
    accion = sys.argv[1] if len(sys.argv) > 1 else None
    gestionar_contador(accion)