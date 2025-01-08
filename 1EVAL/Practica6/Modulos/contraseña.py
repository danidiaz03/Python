def validarContraseña(contra):
    # Validar longitud mínima de 8 caracteres
    if len(contra) < 8:
        return "La contraseña debe tener mínimo 8 caracteres"
    
    # Validar que no contenga espacios
    if " " in contra:
        return "La contraseña no puede contener espacios en blanco"
    
    # Inicializar banderas para las validaciones
    tiene_minuscula = False
    tiene_mayuscula = False
    tiene_numero = False
    tiene_caracter_especial = False
    
    # Recorrer cada caracter de la contraseña
    for c in contra:
        if c.islower():
            tiene_minuscula = True
        elif c.isupper():
            tiene_mayuscula = True
        elif c.isdigit():
            tiene_numero = True
        elif not c.isalnum():  # Si no es alfanumérico, es un carácter especial
            tiene_caracter_especial = True
    
    # Verificar si todas las condiciones se cumplen
    if not tiene_minuscula:
        return "La contraseña debe contener al menos una letra minúscula"
    if not tiene_mayuscula:
        return "La contraseña debe contener al menos una letra mayúscula"
    if not tiene_numero:
        return "La contraseña debe contener al menos un número"
    if not tiene_caracter_especial:
        return "La contraseña debe contener al menos un carácter no alfanumérico"
    
    # Si pasa todas las validaciones, es una contraseña válida
    return True

