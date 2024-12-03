cadena=input("Introduce una cadena de palabras\n")

palabras=cadena.split()
capital=" ".join([palabra.title() for palabra in palabras])
print(capital)