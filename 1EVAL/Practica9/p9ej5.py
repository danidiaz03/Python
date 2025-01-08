import csv

def generar_cuentas(alumnos_csv, cuentas_csv):
    # Leer el listado de alumnos
    alumnos = []
    try:
        with open(alumnos_csv, mode="r", encoding="iso-8859-1") as f:  # Usa la codificación correcta
            lector = csv.reader(f, delimiter=';')
            try:
                encabezado = next(lector)  # Saltar encabezados
                if not encabezado:
                    print(f"El archivo {alumnos_csv} no contiene encabezados.")
                    return
            except StopIteration:
                print(f"El archivo {alumnos_csv} está vacío.")
                return  # Salir si el archivo está vacío

            for linea in lector:
                if len(linea) >= 3:  # Asegurar al menos tres columnas
                    nombre, apellido1, apellido2 = linea[:3]
                    if not nombre.strip() or not apellido1.strip():
                        print(f"Línea con datos faltantes: {linea}")
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
        print("Procesamiento completado.")
    
    # Crear un conjunto para almacenar las cuentas existentes
    cuentas_existentes = set()
    
    try:
        # Leer el archivo de cuentas existentes si existe
        with open(cuentas_csv, mode="r", encoding="UTF-8") as f:
            lector = csv.reader(f, delimiter=';')
            try:
                encabezado = next(lector)  # Saltar encabezados
                if not encabezado:
                    print(f"El archivo {cuentas_csv} no contiene encabezados.")
                    return
            except StopIteration:
                print(f"El archivo {cuentas_csv} está vacío. Se generarán nuevas cuentas.")
                
            for linea in lector:
                cuentas_existentes.add(linea[0])  # Añadir la cuenta a un conjunto para evitar duplicados
    except FileNotFoundError:
        print(f"No se encontró el archivo {cuentas_csv}. Se generará desde cero.")
    
    # Generar cuentas para los alumnos
    nuevas_cuentas = []
    for alumno in alumnos:
        base_cuenta = f"{alumno['nombre'].lower()}.{alumno['apellido1'].lower()}"
        cuenta = f"{base_cuenta}@estudiantes.plaza.com"

        # Si ya existe, usar el formato con el segundo apellido
        if cuenta in cuentas_existentes:
            cuenta = f"{base_cuenta}.{alumno['apellido2'].lower()}@estudiantes.plaza.com"

        cuentas_existentes.add(cuenta)  # Añadir cuenta generada al conjunto de cuentas
        nuevas_cuentas.append(cuenta)
    
    # Escribir las cuentas nuevas en el archivo de cuentas
    with open(cuentas_csv, mode="w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f, delimiter=';')
        escritor.writerow(["Cuenta"])  # Encabezado
        for cuenta in cuentas_existentes:
            escritor.writerow([cuenta])
    
    print("Cuentas generadas y actualizadas en el archivo:", cuentas_csv)

# Uso del programa
alumnos_csv = "ListadoAlumnosFP.csv"
cuentas_csv = "CuentasGeneradas.csv"

generar_cuentas(alumnos_csv, cuentas_csv)

