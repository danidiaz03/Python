def calcular1 (segundos):
    horas = segundos // 3600
    
    # Calcular minutos restantes después de quitar las horas
    minutos = (segundos % 3600) // 60
    
    # Calcular segundos restantes después de quitar las horas y minutos
    segundos = segundos % 60
    
    
    print(f"{horas} horas {minutos} minutos {segundos} segundos")
    

def calcular2(minutos,horas,segundos):
    segundostot=(horas*3600)+minutos*60+segundos
    
    return segundostot

def validarMinutSeg(num):
    if num>59 or num<0:
        return False
    return True

def validarPositivo(num):
    if num<0:
        return False
    return True
    


opcion=int(input("Selecciona opcion:\n 1:Pasar de segundos a horas/minutos/segundos\n 2:Pasar de horas,minutos y segundos a segundos\n"))


if opcion==1:
    segundos=int(input("Introduce segundos a convertir: "))
    calcular1(segundos)    
    
elif opcion==2:
    horas=int(input("Introduce horas: "))
    if validarPositivo(horas):
        minutos=int(input("Introduce los minutos: "))
        if validarMinutSeg(minutos):
            segundos=int(input("Introduce los segundos: "))
            if validarMinutSeg(segundos):
                segundostot=calcular2(minutos,horas,segundos)
                print(f"Son {segundostot} segundos")
            else:
                print("Los segundos no pueden ser negativos ni mayores a 59")
        else:
            print("Los minutos no pueden ser negativos ni mayores a 59")
    else:
        print("Las horas no pueden ser negativas")
else:
    print("Opcion no valida")
        