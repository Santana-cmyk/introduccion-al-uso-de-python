from datos import jugadores

"""
Nombre: Daniel Santana Bueno
Ejercicio 05
Muestra la lista de los jugadores que saben hacer la filigrana "ruleta".
"""

jugadores_ruleta = [jugador for jugador in jugadores if "ruleta" in jugador["filigranas"]]

print(jugadores_ruleta)