diccionario={
}


while True:
    
    palabra=input("Introduce palabra en español / -1 para salir\n")
    
    if palabra =='-1':
        break
    
    traducida=input("Introduce la palabra traducida a inglés\n")
    traducida=traducida.lower()
    palabra=palabra.lower()
    if palabra not in diccionario:
        diccionario[palabra]=traducida
    else:
        print(f'Ya existe la palabra' + {palabra})
        
        
print(diccionario)

frase=input("Introduce frase a traducir: \n")

palabras=frase.lower().split()

traduccion=''

for palabra in palabras:
    if palabra in diccionario.keys():
        traduccion+=diccionario[palabra] + " "
    else:
        traduccion+=palabra + " "

print(traduccion)