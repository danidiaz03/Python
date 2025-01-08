cadena=input("Introduce una cadena: ")

contador={}

#Hacemos un array de palabras
palabras=cadena.lower().split()  

#recorremos el array
for palabra in palabras:
    
    #quitamos signos
    palabra=palabra.strip('.,!?;:')
    
    #si la palabra esta en el diccionario suma 1
    if palabra in contador:
        contador[palabra]+=1
    
    #si no la inicializa en 1
    else:
        contador[palabra]=1
        
print(contador)