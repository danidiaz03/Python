minutos =int(input ("introduce los minutos a convertir"))

horas=(minutos//60)
minutos_rest=minutos%60
print(f"{minutos} minutos son {horas} horas y {minutos_rest} minutos")
