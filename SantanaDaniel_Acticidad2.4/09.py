from datos import jugadores

"""
Nombre: Daniel Santana Bueno
Ejercicio 09
Muestra una lista con los nombres de los jugadores que dominan más de 2 filigranas
distintas.
"""

filigranas2 = [
    jugador["nombre"] for jugador in jugadores if len(jugador["filigranas"]) > 2
]

print(filigranas2)
