def dibujar(caracter,ancho,alto):
    
    for i in range (0,alto):
        fila=''
        for i in range (0,ancho):
            fila+=caracter
        print(fila)    
            
        

caracter=input("Introduce caracter : ")

ancho=int(input("Introduce el ancho del rectángulo : "))
alto=int(input("Introduce el alto del rectángulo : "))

dibujar(caracter,ancho,alto)