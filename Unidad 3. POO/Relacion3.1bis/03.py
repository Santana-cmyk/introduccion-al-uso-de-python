EURO_DOLAR = 1.09
EURO_YEN = 163.38
DOLAR_EURO = 0.92
DOLAR_YEN = 149.67
YEN_EURO = 0.0061
YEN_DOLAR = 0.0067

def cambiar_divisa (cantidad: float, divisa_a :str, divisa_b : str) -> float:
    divisa_a = divisa_a.lower()
    divisa_b = divisa_b.lower()

    cantidad_cambiada = 0

    if divisa_a == "euro":
        if divisa_b == "dolar":
            cantidad_cambiada = cantidad * EURO_DOLAR
        elif divisa_b == "yen":
            cantidad_cambiada = cantidad * EURO_YEN
    elif divisa_a == "dolar":
        if divisa_b == "euro":
            cantidad_cambiada = cantidad * DOLAR_EURO
        elif divisa_b == "yen":
            cantidad_cambiada = cantidad * DOLAR_YEN
    elif divisa_a == "yen":
        if divisa_b == "euro":
            cantidad_cambiada = cantidad * YEN_EURO
        elif divisa_b == "dolar":
            cantidad_cambiada = cantidad * YEN_DOLAR

    return round(cantidad_cambiada,3)

print(cambiar_divisa(10,"euro","yen"))