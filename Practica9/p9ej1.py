# listin.py
import os

LISTIN_FILE = "listin.txt"

def inicializar_listin():
    if not os.path.exists(LISTIN_FILE):
        with open(LISTIN_FILE, "w") as f:
            pass  # Crea el archivo vacío

def consultar_cliente(nombre):
    with open(LISTIN_FILE, "r") as f:
        for linea in f:
            cliente, telefono = linea.strip().split(",")
            if cliente == nombre:
                return telefono
    return None

def añadir_cliente(nombre, telefono):
    with open(LISTIN_FILE, "a") as f:
        f.write(f"{nombre},{telefono}\n")

def eliminar_cliente(nombre):
    lineas = []
    encontrado = False
    with open(LISTIN_FILE, "r") as f:
        for linea in f:
            cliente, _ = linea.strip().split(",")
            if cliente != nombre:
                lineas.append(linea)
            else:
                encontrado = True
    with open(LISTIN_FILE, "w") as f:
        f.writelines(lineas)
    return encontrado

# Ejemplo de uso

inicializar_listin()
añadir_cliente("Juan", "123456789")
print(consultar_cliente("Juan"))  # Salida: 123456789
eliminar_cliente("Juan")
print(consultar_cliente("Juan"))  # Salida: None