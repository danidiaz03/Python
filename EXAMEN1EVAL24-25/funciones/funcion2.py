#DANIEL DIAZ
def funcion2a(fichero):
    sitios = []
    with open(fichero, "r") as f:
        for linea in f:
            datos= linea.strip()
            sitios.append(datos)
        
    return sitios

def funcion2b(personas,sitios):
    lista=list((x[0]) for x in personas.items() for c in x[1] if c not in sitios)
    lista_unica=[]
    for x in lista:
        if x not in lista_unica:
            lista_unica.append(x)
    return lista_unica

def funcion2bMostrar(personas,sitios):
    lista=funcion2b(personas,sitios)
    for x in lista:
        print(x)
    