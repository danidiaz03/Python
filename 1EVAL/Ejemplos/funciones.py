def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

print(factorial(5))


cuadrado=lambda x:x**2
print(cuadrado(10))

#MAP
numeros=[1,2,3,4]
cuadrados=map(lambda x:x**2,numeros)
print(list(cuadrados))


#FILTER
numeros=[1,2,3,4,5]
pares=filter(lambda x:x%2==0,numeros)
print(list(pares))

#REDUCE
from functools import reduce
numeros=[1,2,3,4]
producto=reduce(lambda x, y:x*y, numeros)
print(producto)

#LIST COMPREHENSION
cubos=[x**3 for x in [1,2,3,4,5]]
print(cubos)

pares=[x for x in range(10) if x%2==0]
print(pares)

combinaciones=[x + y for x in [1,2,3] for y in [4,5,6]]
print(combinaciones)

#ficheros python del directorio actual
import os
ficheros_python=[f for f in os.listdir(os.path.dirname(os.path.abspath(__file__)))if f.endswith('.py')]
print(ficheros_python)

num_doble_cuadrado=[(num,num*2,num**2)for num in range(10)]
print(num_doble_cuadrado)