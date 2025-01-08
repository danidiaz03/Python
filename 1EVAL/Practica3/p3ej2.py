def seleccionar_caracter():
    """
    Función que pide al usuario un carácter o usa '*' por defecto.
    """
    caracter = input("Introduce un carácter para dibujar el triángulo (o presiona Enter para usar '*'): ")
    if caracter == "":
        return "*"
    return caracter

def dibujar_triangulo(anchura, caracter):
    """
    Función que dibuja un triángulo con la anchura proporcionada y el carácter seleccionado.
    """
    # Parte creciente del triángulo
    for i in range(1, anchura + 1):
        print(caracter * i)
    
    # Parte decreciente del triángulo
    for i in range(anchura - 1, 0, -1):
        print(caracter * i)

# Solicitar al usuario la anchura del triángulo
anchura = int(input("Introduce la anchura del triángulo: "))

# Llamar a la función seleccionar_caracter para obtener el carácter a usar
caracter = seleccionar_caracter()

# Llamar a la función dibujar_triangulo para dibujar el triángulo
dibujar_triangulo(anchura, caracter)