
nombresList=[]
nombre='0'
nombresdistList=[]

while(nombre!='-1'):
    nombre=input("Introduce un nombre: ")
    if nombre == '-1':
        break
    nombresList.append(nombre)
    if nombre not in nombresdistList:
        nombresdistList.append(nombre)
    
print(nombresList)
print(nombresdistList)

for nombre in nombresdistList:
    veces=nombresList.count(nombre)
    print(nombre+ f': {veces}')