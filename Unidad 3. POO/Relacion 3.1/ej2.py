"""
Nombre: Daniel Santana Bueno

Desc: Crea una función llamada convertirTemperatura que reciba un número con
decimales y dos cadenas de caracteres. Las cadenas de caracteres posibles
serán “C”, “K” y “F”, que representan unidades de temperatura (Celsius,
Kelvin y Fahrenheit). La función devolverá, como número con decimales, el
resultado de convertir de la primera unidad que reciba la función a la
segunda. Por ejemplo, convertirTemperatura(10,”F”,”C”) devolvería el
resultado de pasar 10 Fahrenheit a Celsius. Devuelve el resultado con dos
decimales, redondeando al valor más cercano.
"""

def convertirTemperatura(temperatura, origen, destino):
    if origen == destino:
        return round(float(temperatura), 2)

    if origen == "F":
        temperatura = (temperatura - 32) * 5 / 9
    elif origen == "K":
        temperatura = temperatura - 273.15

    if destino == "F":
        temperatura = temperatura * 9 / 5 + 32
    elif destino == "K":
        temperatura = temperatura + 273.15

    return round(temperatura, 2)
