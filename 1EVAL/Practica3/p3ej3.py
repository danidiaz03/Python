def seleccionar_caracter_subrayado():
    """
    Función que pide al usuario un carácter para subrayar el texto o usa '=' por defecto.
    """
    caracter = input("Introduce un carácter para subrayar el texto (o presiona Enter para usar '='): ")
    if caracter == "":
        return "="
    return caracter

def EscribirCentrado(texto, caracter_subrayado="="):
    """
    Función que recibe un texto y lo escribe centrado en una pantalla de 80 columnas.
    Luego subraya el texto usando el carácter proporcionado o el carácter por defecto '='.
    """
    anchura_pantalla = 20
    # Calcula cuántos espacios hay que añadir a la izquierda para centrar el texto
    espacios_izquierda = (anchura_pantalla - len(texto)) // 2
    
    # Escribe el texto centrado
    print(" " * espacios_izquierda + texto)
    
    # Subraya el texto con el carácter elegido
    print(" " * espacios_izquierda + caracter_subrayado * len(texto))

# Solicitar el texto al usuario
texto = input("Introduce el texto que quieres centrar: ")

# Solicitar el carácter para subrayar
caracter_subrayado = seleccionar_caracter_subrayado()

# Llamar a la función para escribir el texto centrado y subrayado
EscribirCentrado(texto, caracter_subrayado)