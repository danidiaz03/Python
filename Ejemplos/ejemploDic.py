diccionario_1=dict()
diccionario_2={}
diccionario_3={'Francia':'frances','España':'español'}
diccionario_4={'España':['Madrid',7777777,6666],}

#Lista entera
print(diccionario_4['España'])
#la capital
print(diccionario_4['España'][0])

#Cambio poblacion
diccionario_4['España'][1]=49000000

diccionario_5={
    'España':{'capital':'Madrid',
              'poblacion':49000000,
              'superficie':888888
              },
    'Francia':{'capital':'Paris',
              'poblacion':66666213,
              'superficie':54455
    }
}

print(len(diccionario_5))
print(len(diccionario_5['España']))

pais=input('Introduce un pais europeo: ')
if pais in diccionario_5:
    print('SI lo tengo registrado')
else:
    print('No lo tengo registrado')
    
#Escribo los nombres de los paises

for p in diccionario_5:
    print(p)

for p in diccionario_5.keys():
    print(p)

#todos los datos de cada pais
for p in diccionario_5:
    print(diccionario_5[p])


for p in diccionario_5.values():
    print(p)   
    
#todo el diccionario
for p in diccionario_5.items():
    print(p)

#la poblacion de todos los paises
for p in diccionario_5:
    print(str(p) + " - " +str(diccionario_5[p]['poblacion']))
    
for p in diccionario_5.items():
    print(str(p[0])+ " - " + str(p[1]['poblacion']))
    
    
    
for c,v in zip(diccionario_5.keys(),diccionario_5.values()):
    print(str(c)+" - " +str(v['poblacion']))