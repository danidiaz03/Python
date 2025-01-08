def filtrar_palabras(lista,n):
    for palabra in lista:
        if len(palabra)>=n:
            print(palabra)


lista=['isi','james','alvaro','camello','rdt']

filtrar_palabras(lista,4)