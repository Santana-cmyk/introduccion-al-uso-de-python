"""
 Nombre: Daniel Santana Bueno

Desc: Crea una función llamada comprobarLetraDNI que reciba una cadena de
 caracteres que representará al DNI de una persona y devuelva True si el DNI
 es correcto y False si no lo es. Un DNI es correcto si tiene 8 dígitos enteros
 seguidos de una letra (mayúscula o minúscula), y la letra es correcta. Para
 conocer si la letra es correcta puedes consultar la web del Ministerio del
 Interior.
"""


def comprobarLetraDNI(dni):
    if len(dni) != 9:
        return False

    numero = dni[0:8]
    for digito in numero:
        if digito not in "0123456789":
            return False

    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    letra_correcta = letras[int(numero) % 23]
    return dni[8].upper() == letra_correcta

