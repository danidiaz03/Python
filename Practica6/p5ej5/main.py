import ModuloFechas.FuncionesFechas as ff

# Ejemplo 1: Año, Mes y Día
print(ff.Year(20200903))  # "2020"
print(ff.month(20200903))  # "09"
print(ff.monthName(20200903))  # "septiembre"
print(ff.day(20200903))  # "03"

# Ejemplo 2: Formatos de Fechas
print(ff.date2Text(20200903))  # "03/09/2020"
print(ff.date2TextName(20200903))  # "3 de septiembre de 2020"

# Ejemplo 3: Varias Fechas
print(ff.manyDates(202009032020090420200903))
# "\n03/09/2020\n04/09/2020\n03/09/2020"

# Ejemplo 4: Comparar Fechas
print(ff.sameDates(202009032021090420200903, 21000903))  # 2
