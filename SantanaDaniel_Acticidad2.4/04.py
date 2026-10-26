from datos import jugadores

"""
Nombre: Daniel Santana Bueno
Ejercicio 04
Muestra una lista con los nombres de los jugadores que tienen una puntuación de
pase igual o superior a 9 en sus atributos.
"""

jugadores_superior9 = [jugador for jugador in jugadores if jugador["atributos"]["pase"] >= 9]

print(jugadores_superior9)
