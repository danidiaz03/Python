# personas.py
def leer_personas(fichero):
    personas = []
    with open(fichero, "r") as f:
        for linea in f:
            id_, nombre, apellido, fecha = linea.strip().split(";")
            personas.append({
                "id": id_,
                "nombre": nombre,
                "apellido": apellido,
                "fecha_nacimiento": fecha
            })
    return personas

# Ejemplo de uso
if __name__ == "__main__":
    personas = leer_personas("personas.txt")
    for persona in personas:
        print(persona)