def validarUsuario(usuario):
    if(len(usuario)>=6 and len(usuario)<=12):
        if usuario.isalnum():
            return True
        else:
            print("El nombre de usuario puede contener solo letras y números")
            return False
    else:
        if len(usuario)<6:
            print("El nombre de usuario debe contener al menos 6 caracteres")
        if len(usuario)>12:
            print("El nombre de usuario no puede contener más de 12 caracteres")
        return False