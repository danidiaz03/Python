import random


numero=random.randint(0, 9)

maxintentos=3
contintentos=1
acertado=False

while(acertado==False):
    
    if contintentos<=maxintentos:
        num=float(input("Introduce un número:  "))
        if num != numero:
            print("No has acertado")
            contintentos+=1
        else:
            acertado=True 
            print(f"Has acertado!!!! Has necesitado {contintentos} intentos")
            
    else:
        print("Numero de intentos alcanzado")
        break