from . import FuncionesAuxiliares

import calendar

def longitud(fecha):
    """Verifica si la fecha tiene exactamente 8 dígitos."""
    return len(str(fecha)) == 8

def Year(fecha):
    """Devuelve el año de la fecha o 'Formato no válido' si no cumple el requisito."""
    if longitud(fecha):
        return FuncionesAuxiliares.extraer_anio(fecha)
    return "Formato no valido"

def month(fecha):
    """Devuelve el mes de la fecha o 'Mes incorrecto' si no es válido."""
    if longitud(fecha):
        mes = FuncionesAuxiliares.extraer_mes(fecha)
        if FuncionesAuxiliares.es_mes_valido(mes):
            return mes
        return "Mes incorrecto"
    return "Formato no valido"

def monthName(fecha):
    """Devuelve el nombre del mes o 'Formato no válido' si el mes no es válido."""
    if longitud(fecha):
        mes = month(fecha)
        if mes.isdigit():
            meses = [
                "enero", "febrero", "marzo", "abril", "mayo", "junio",
                "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
            ]
            return meses[int(mes) - 1]
    return "Formato no valido"

def day(fecha):
    """Devuelve el día de la fecha o 'FECHA INCORRECTA' si no es válido."""
    if longitud(fecha):
        anio = int(FuncionesAuxiliares.extraer_anio(fecha))
        mes = int(FuncionesAuxiliares.extraer_mes(fecha))
        dia = int(FuncionesAuxiliares.extraer_dia(fecha))
        if 1 <= mes <= 12:
            max_dia = calendar.monthrange(anio, mes)[1]
            if 1 <= dia <= max_dia:
                return f"{dia:02d}"  # Formato con 2 dígitos
    return "FECHA INCORRECTA"

def date2Text(fecha):
    """Devuelve la fecha en formato 'DD/MM/AAAA' o 'FECHA INCORRECTA'."""
    if longitud(fecha):
        anio = Year(fecha)
        mes = month(fecha)
        dia = day(fecha)
        if mes.isdigit() and dia.isdigit():
            return f"{dia}/{mes}/{anio}"
    return "FECHA INCORRECTA"

def date2TextName(fecha):
    """Devuelve la fecha en formato 'D de MES de AÑO' o 'FECHA INCORRECTA'."""
    if longitud(fecha):
        anio = Year(fecha)
        mes_nombre = monthName(fecha)
        dia = day(fecha)
        if dia.isdigit() and mes_nombre not in ["Formato no valido", "FECHA INCORRECTA"]:
            return f"{int(dia)} de {mes_nombre} de {anio}"
    return "FECHA INCORRECTA"

def manyDates(fechas):
    """Devuelve un texto con varias fechas en formato 'DD/MM/AAAA' separadas por '\n'."""
    lista_fechas = FuncionesAuxiliares.extraer_fechas(fechas)
    resultado = []
    for fecha in lista_fechas:
        if longitud(fecha):
            texto_fecha = date2Text(int(fecha))
        else:
            texto_fecha = "FECHA INCORRECTA"
        resultado.append("\n" + texto_fecha)
    return "".join(resultado)

def sameDates(fechas, fecha_base):
    """Devuelve la cantidad de fechas con el mismo día y mes que la fecha base."""
    lista_fechas = FuncionesAuxiliares.extraer_fechas(fechas)
    base_dia = FuncionesAuxiliares.extraer_dia(fecha_base)
    base_mes = FuncionesAuxiliares.extraer_mes(fecha_base)
    count = 0
    for fecha in lista_fechas:
        if longitud(fecha):
            dia = FuncionesAuxiliares.extraer_dia(int(fecha))
            mes = FuncionesAuxiliares.extraer_mes(int(fecha))
            if dia == base_dia and mes == base_mes:
                count += 1
    return count
