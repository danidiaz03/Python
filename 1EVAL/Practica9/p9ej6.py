import csv

# Función a: Leer y devolver lista de diccionarios ordenada por apellidos
def leer_calificaciones(fichero):
    alumnos = []
    with open(fichero, mode="r", encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=';')
        encabezados = next(lector)  # Leer encabezados y descartarlos

        for linea in lector:
            if len(linea) != len(encabezados):  # Ignorar líneas mal formadas
                continue
            
            apellido, nombre, asistencia, parcial1, parcial2, ordinario1, ordinario2, practicas, ordinario_practicas = linea
            
            # Convertir calificaciones a flotantes o vacíos si no hay valor
            parcial1 = float(parcial1.replace(",", ".")) if parcial1 else None
            parcial2 = float(parcial2.replace(",", ".")) if parcial2 else None
            practicas = float(practicas.replace(",", ".")) if practicas else None
            ordinario1 = float(ordinario1.replace(",", ".")) if ordinario1 else None
            ordinario2 = float(ordinario2.replace(",", ".")) if ordinario2 else None
            ordinario_practicas = float(ordinario_practicas.replace(",", ".")) if ordinario_practicas else None

            alumnos.append({
                "nombre": nombre,
                "apellido": apellido,
                "asistencia": int(asistencia.strip('%')),  # Convertir asistencia a porcentaje entero
                "calificaciones": {
                    "parcial1": parcial1,
                    "parcial2": parcial2,
                    "ordinario1": ordinario1,
                    "ordinario2": ordinario2,
                    "practicas": practicas,
                    "ordinario_practicas": ordinario_practicas
                }
            })
    
    # Ordenar por apellidos
    alumnos.sort(key=lambda x: x["apellido"])
    return alumnos

# Función b: Calcular la nota final y agregarla al diccionario
def calcular_notas_finales(alumnos):
    for alumno in alumnos:
        calificaciones = alumno["calificaciones"]

        # Usar la mejor calificación entre el examen inicial y la convocatoria ordinaria
        parcial1 = max(calificaciones["parcial1"] or 0, calificaciones["ordinario1"] or 0)
        parcial2 = max(calificaciones["parcial2"] or 0, calificaciones["ordinario2"] or 0)
        practicas = max(calificaciones["practicas"] or 0, calificaciones["ordinario_practicas"] or 0)

        # Calcular la nota final
        nota_final = 0.3 * parcial1 + 0.3 * parcial2 + 0.4 * practicas
        alumno["nota_final"] = round(nota_final, 2)

# Función c: Dividir alumnos en aprobados y suspensos
def clasificar_alumnos(alumnos):
    aprobados = []
    suspensos = []

    for alumno in alumnos:
        asistencia = alumno["asistencia"]
        calificaciones = alumno["calificaciones"]

        parcial1 = max(calificaciones["parcial1"] or 0, calificaciones["ordinario1"] or 0)
        parcial2 = max(calificaciones["parcial2"] or 0, calificaciones["ordinario2"] or 0)
        practicas = max(calificaciones["practicas"] or 0, calificaciones["ordinario_practicas"] or 0)
        nota_final = alumno["nota_final"]

        # Criterios de aprobación
        if (
            asistencia >= 75 and
            parcial1 >= 4 and
            parcial2 >= 4 and
            practicas >= 4 and
            nota_final >= 5
        ):
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)
    
    return aprobados, suspensos

# Uso del programa
fichero = "calificaciones.csv"
alumnos = leer_calificaciones(fichero)
calcular_notas_finales(alumnos)
aprobados, suspensos = clasificar_alumnos(alumnos)

# Resultados
print("Aprobados:")
for alumno in aprobados:
    print(f"{alumno['apellido']} {alumno['nombre']} - Nota Final: {alumno['nota_final']}")

print("\nSuspensos:")
for alumno in suspensos:
    print(f"{alumno['apellido']} {alumno['nombre']} - Nota Final: {alumno['nota_final']}")
