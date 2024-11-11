def validarContraseña(contra):
    if len(contra)>=8:
        return True
    else:
        print("La contraseña debe tener mínimo 8 carácteres")
        return False