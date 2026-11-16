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

    """Convierte una temperatura entre Celsius, Fahrenheit y Kelvin.

    Args:
        temperatura: Valor numérico de la temperatura que se convertirá.
        origen: Unidad original ("C", "F" o "K").
        destino: Unidad de destino ("C", "F" o "K").

    Returns:
        La temperatura convertida, redondeada a dos decimales.

    Raises:
        ValueError: Si la unidad de origen o de destino no es válida.
    """

    
    if origen == "C":
        celsius = temperatura
    elif origen == "F":
        celsius = (temperatura - 32) * 5 / 9
    elif origen == "K":
        celsius = temperatura - 273.15
    else:
        raise ValueError("La unidad de origen debe ser 'C', 'F' o 'K'.")

    if destino == "C":
        resultado = celsius
    elif destino == "F":
        resultado = celsius * 9 / 5 + 32
    elif destino == "K":
        resultado = celsius + 273.15
    else:
        raise ValueError("La unidad de destino debe ser 'C', 'F' o 'K'.")

    return round(resultado, 2)
