def convertir_acciones(compania: str, numero_acciones: int, moneda_cambio: str) -> float:
    compania = compania.upper()
    moneda_cambio = moneda_cambio.upper()

    if compania == "NVDA":
        precio = 156.20
    elif compania == "SONY":
        precio = 24.16
    elif compania == "BMW":
        precio = 58.12

    if moneda_cambio == "EURO":
        cambio = 1.00
    elif moneda_cambio == "DOLAR":
        cambio = 1.10
    elif moneda_cambio == "LIBRA":
        cambio = 0.83
    else:
        raise ValueError("Solo se admite el EURO, DOLAR y la LIBRA")

    resultado = (numero_acciones * cambio * precio)
    return round(resultado, 2)


print(convertir_acciones("NVDA", 10, "EURO"))
print(convertir_acciones("SONY", 5, "DOLAR"))
print(convertir_acciones("BMW", 20, "libra" ))
