

def esVocal(l):
    vocales=['A','E','I','O','U']
    return l in vocales
       
 
def estaEnLista(l,lista):
    for i in range(0,len(lista)):
        if lista[i][0]==l:
            return i
    return -1

def transformar(lista_frecuencias):
    listaf_tuplas=[]
    for item in lista_frecuencias:
        listaf_tuplas.append((item[0],item[1]))
    return listaf_tuplas


palabra=input("Introduce")
letras=list(palabra.upper())
lista_frecuencias=[]
for l in letras:
    if esVocal(l):
        p=estaEnLista(l,lista_frecuencias)
        if p!=-1:
            lista_frecuencias[p][1]+=1
            
        else:
            lista_frecuencias.append([l,1])
          
print(lista_frecuencias)
lista_frecuencias=transformar(lista_frecuencias)
print(lista_frecuencias)
lista_frecuencias.sort(key=lambda x:x[1],reverse=True)
print(lista_frecuencias)

