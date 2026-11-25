"""
racha

Recibe una lista de puntuaciones enteras y un mínimo (10 por defecto). Busca
el tramo consecutivo más largo con puntuaciones mayores o iguales al mínimo.
Devuelve el índice inicial y la longitud. Si hay empate, conserva el primer
tramo. Si no hay ninguno, devuelve (-1, 0).
"""

def buscar_racha(puntuaciones, minimo=10):
    mejor_inicio = -1
    mejor_longitud = 0
    longitud = 0
    for indice, puntuacion in enumerate(puntuaciones):
        if puntuacion >= minimo:
            longitud += 1
            if longitud > mejor_longitud:
                mejor_inicio = indice - longitud + 1
                mejor_longitud = longitud
        else:
            longitud = 0
    return mejor_inicio, mejor_longitud


if __name__ == "__main__":
    assert buscar_racha([9, 11, 10, 2, 10, 12]) == (1, 2)
    assert buscar_racha([12, 2, 11, 12, 13]) == (2, 3)
    assert buscar_racha([1, 5, 5], 5) == (1, 2)
    assert buscar_racha([9]) == (-1, 0)
    assert buscar_racha([]) == (-1, 0)
