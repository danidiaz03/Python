def calcular_comision(retiro):
    if retiro < 1000:
        return 10
    else:
        comision_base = 10
        unidades_extra = (retiro // 1000)  # Número de unidades o fracciones de 1000€
        return comision_base + (unidades_extra * 10)

# Solicitar la cantidad a retirar al usuario
try:
    cantidad_retirada = float(input("Introduce la cantidad a retirar: "))
    if cantidad_retirada < 0:
        raise ValueError("La cantidad a retirar no puede ser negativa.")

    comision = calcular_comision(cantidad_retirada)
    print(f"La comisión por retirar {cantidad_retirada}€ es de {comision}€.")
except ValueError as e:
    print(f"Error: {e}")