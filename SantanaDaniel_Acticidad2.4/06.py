from datos import jugadores

"""
Nombre: Daniel Santana Bueno
Ejercicio 06
Muestra una lista con los jugadores que tienen tiro >= 8 Y regate >= 9.
"""
jugadores_tiro_pase = [
    jugador
    for jugador in jugadores
    if jugador["atributos"]["tiro"] >= 8 and jugador["atributos"]["regate"] >= 9
]

print(jugadores_tiro_pase)
