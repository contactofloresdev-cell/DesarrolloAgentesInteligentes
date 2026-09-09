def cambio_voraz(monedas, cantidad):
    monedas.sort(reverse=True)  # Ordena de mayor a menor
    resultado = {}

    for moneda in monedas:
        if cantidad >= moneda:
            num_monedas = cantidad // moneda
            cantidad -= num_monedas * moneda
            resultado[moneda] = num_monedas

    return resultado


# Ejemplo
monedas = [1, 5, 10, 25]
cantidad = 63
print(cambio_voraz(monedas, cantidad))
