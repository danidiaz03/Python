lista=['isi','james','isi','alvaro','camello','camello']

cadena=input("Introduce palabra a buscar: ")

if cadena in lista:
    print(f"Existe en la lista {lista.count(cadena)} veces")
    cadena2=input("Introduce palabra2 para sustituir: ")
    indice=lista.index(cadena)
    lista.insert(indice,cadena2)
    print(lista)
    lista.remove(cadena)
    print(lista)
    
else:
    print(cadena+" no está en la lista")

