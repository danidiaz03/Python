from Modulos.usuario import validarUsuario

while True:
    usuario=input('Introduce nombre de usuario\n')
    if(validarUsuario(usuario)):
        break
    
print("Usuario correcto")
    
    
