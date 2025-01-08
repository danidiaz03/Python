def ConvertirEspaciado(texto, num_espacios=1):
    """
    Función que recibe un texto y devuelve una cadena con un número adicional
    de espacios tras cada letra. El número de espacios es 1 por defecto, pero
    el usuario puede indicar más.
    """
    # Crea una cadena de espacios según el número indicado
    espacio = " " * num_espacios
    # Añade los espacios entre cada carácter, usando join para combinar la lista
    texto_espaciado = espacio.join(texto)
    return texto_espaciado

# Solicitar el texto al usuario
texto = input("Introduce el texto que quieres espaciar: ")

# Preguntar si el usuario quiere un número específico de espacios
respuesta = input("¿Quieres definir el número de espacios entre cada letra? (s/n): ")

if respuesta.lower() == 's':
    num_espacios = int(input("Introduce el número de espacios: "))
    # Llamar a la función con el número de espacios indicado
    texto_convertido = ConvertirEspaciado(texto, num_espacios)
else:
    # Llamar a la función con 1 espacio por defecto
    texto_convertido = ConvertirEspaciado(texto)

# Imprimir el resultado
print("Texto convertido:", texto_convertido)