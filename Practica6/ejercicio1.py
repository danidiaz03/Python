from Modulos.usuario import validarUsuario
from Modulos.contraseña import validarContraseña

usuarios_contraseñas = {}
otro=True
x=1
while(otro):
   
    print("Usuario " + str(x))

    while True:
        usuario=input('Introduce nombre de usuario o 0 para salir\n')
        if(validarUsuario(usuario)):
            break
    if(usuario=="0"):
        break    
    print("Usuario correcto")
        
    while True:
        contraseña=input('Introduce contraseña\n')
        if(validarContraseña(contraseña)):
            break
        
    print("contraseña correcta")
    
    x=x+1
    usuarios_contraseñas[usuario] = contraseña
    print(f"Usuario '{usuario}' registrado correctamente.\n")    

print(usuarios_contraseñas)