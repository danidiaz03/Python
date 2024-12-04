#DANIEL DIAZ
def funcion1a(fichero):
    personas = {}
    with open(fichero, "r") as f:
        for linea in f:
            datos= linea.strip().split("|")
            if datos[0] not in personas:
                personas[datos[0]]=[datos[1]]
            else:
                if datos[1] not in personas[datos[0]]:
                    personas[datos[0]].append(datos[1])
    return personas

def funcion1b(personas):
    for c,v in zip(personas.keys(),personas.values()):
        print(str(c)+" : " +str(v))