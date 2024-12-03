from Modulos.usuario import validarUsuario
from Modulos.contraseña import validarContraseña

usuarios_contraseñas = {}
otro=True
x=1
while(otro):
   
    print("Usuario " + str(x))

    while True:
        usuario=input('Introduce nombre de usuario o * para salir\n')
        if usuario in usuarios_contraseñas:
            print(f"Ya existe el usuario {usuario}")
        else:
            if(validarUsuario(usuario)):
                break
            
    if(usuario=="*"):
        break    
    print("Usuario correcto")
    
    valido=False
    
    while valido==False:
        contraseña=input('Introduce contraseña\n')
        existe=False
        for p in usuarios_contraseñas:
            if usuarios_contraseñas[p]["contraseña"]==contraseña:
                print("La contraseña "+contraseña+ " ya ha sido utilizada")
                existe=True
                break
        if existe==False:
            if(validarContraseña(contraseña)):
                valido=True
            
    print("Contraseña correcta")
    
    usuarios_contraseñas[usuario]=contraseña
    print(f"Usuario '{usuario}' creado correctamente")
    x=x+1              
                
print(usuarios_contraseñas)
