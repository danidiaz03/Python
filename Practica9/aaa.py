import csv

def generar_cuentas(alumnos_csv):
    alumnos = []
    try:
        with open(alumnos_csv, mode="r", encoding="iso-8859-1") as f:  # Usa la codificación correcta
            lector = csv.reader(f, delimiter=';')
            
            # Intentamos leer la primera línea (encabezado)
            encabezado = next(lector, None)
            if encabezado is None:
                print(f"El archivo {alumnos_csv} está vacío o no contiene encabezado.")
                return
            
            print(f"Encabezado: {encabezado}")  # Mostrar el encabezado para verificación

            for linea in lector:
                if len(linea) >= 3:  # Asegurar al menos tres columnas
                    nombre, apellido1, apellido2 = linea[:3]
                    if not nombre.strip() or not apellido1.strip():
                        print(f"Línea con datos faltantes (nombre o primer apellido): {linea}")
                        continue

                    alumnos.append({
                        "nombre": nombre.strip(),
                        "apellido1": apellido1.strip(),
                        "apellido2": apellido2.strip(),
                    })
                else:
                    print(f"Línea incorrecta o incompleta: {linea}. Esperado: al menos 3 columnas.")

    except FileNotFoundError:
        print(f"No se encontró el archivo {alumnos_csv}.")
        return
    except UnicodeDecodeError as e:
        print(f"Error de codificación: {e}")
        return
    finally:
        print(f"Procesamiento completado. Se procesaron {len(alumnos)} alumnos.")

# Ejemplo de uso:
alumnos_csv = "ListadoAlumnosFP.csv"
generar_cuentas(alumnos_csv)
