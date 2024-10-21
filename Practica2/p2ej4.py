import random


numero=random.randint(0, 9)

acertado=False

while(acertado==False):
    num=float(input("Introduce un número:  "))
    if num != numero:
        print("No has acertado")
    else:
        acertado=True
        print("Has acertado!!!!")