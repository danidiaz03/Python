def validarDNI(dni):
    if len(dni) != 9 or not dni[:-1].isdigit() or not dni[-1].isalpha():
        print("DNI no válido. Debe tener 8 dígitos seguidos de una letra.")
        return False
    return True

def validarEdad(edad):
    if edad < 18 or edad >= 100:
        print("La edad debe ser mayor o igual a 18 y menor que 100.")
        return False
    return True
