def sumatorio(numero):
    if type(numero) is not int or numero < 0:
        raise ValueError("El sumatorio requiere un número entero positivo o cero.")

    resultado = 0
    for valor in range(numero + 1):
        resultado += valor
    return resultado


def factorial(numero):
    if type(numero) is not int or numero < 1:
        raise ValueError("El factorial requiere un número entero mayor o igual a 1.")

    resultado = 1
    for valor in range(1, numero + 1):
        resultado *= valor
    return resultado


def aplicar_funcion(valor: int, cadena: str):
    if cadena.lower() == "sumatorio":
        return sumatorio(valor)
    if cadena.lower() == "factorial":
        return factorial(valor)
    raise ValueError("La función debe ser 'sumatorio' o 'factorial'.")


print(aplicar_funcion(3, "FACTORIAL"))
