def clasificar_caracter(caracter):
    if caracter.isdigit():
        return "Es un digito"
    if caracter.isupper():
        return "Es una mayuscula"
    if caracter.islower():
        return "Es una minuscula"

caracter=input("introduce un caracter")

if len(caracter)!=1:
    print("Solo es un caracter")
else:
    resultado=clasificar_caracter(caracter)
    print(resultado)
    
    



    