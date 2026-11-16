"""
Nombre: Daniel Santana Bueno

Desc: Crea una función llamada calcularValorBruto, que reciba un número con
decimales (el precio de un producto) y una cadena de caracteres (que
representará el tipo de IVA aplicable). Las cadenas de caracteres posibles
serán GENERAL, REDUCIDO y SUPERREDUCIDO. La función devolverá el
resultado de sumar el IVA aplicable al valor neto del producto. Por ejemplo,
calcularValorBruto(10,”GENERAL”) devolvería el resultado de sumar a los
10€ de valor neto, el porcentaje de IVA del tipo general (que es un 21%), lo
que daría 12,1€. Devuelve el resultado con dos decimales, redondeando
hacia arriba.
"""

def calcularValorBruto(precio, tipoIVA):
    """Calcula el precio bruto de un producto aplicando el IVA indicado.

    Args:
        precio: Precio neto del producto.
        tipoIVA: Tipo de IVA: "GENERAL", "REDUCIDO" o "SUPERREDUCIDO".

    Returns:
        float: El valor bruto tras aplicar el IVA
    Raises:
        ValueError: Si el tipo de IVA no es válido.
    """
    if tipoIVA == "GENERAL":
        porcentaje = 21
    elif tipoIVA == "REDUCIDO":
        porcentaje = 10
    elif tipoIVA == "SUPERREDUCIDO":
        porcentaje = 4
    else:
        raise ValueError("Tipo de IVA no válido")

    bruto = round(precio * (100 + porcentaje) / 100, 2)
    return bruto
