# palabra_mas_repetida.py
from collections import Counter

def palabra_mas_repetida(fichero):
    with open(fichero, "r") as f:
        palabras = f.read().split()
    conteo = Counter(palabras)
    palabra, frecuencia = conteo.most_common(1)[0]
    return palabra, frecuencia

# Ejemplo de uso
if __name__ == "__main__":
    palabra, frecuencia = palabra_mas_repetida("texto.txt")
    print(f"La palabra más repetida es '{palabra}' con {frecuencia} apariciones.")