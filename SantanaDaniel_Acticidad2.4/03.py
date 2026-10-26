from datos import jugadores

"""
Nombre: Daniel Santana Bueno
Ejercicio 03
Muestra una lista con los nombres de los jugadores que pertenecen al "FC
Barcelona".
"""

barcelona_futbolistas = [jugador for jugador in jugadores if "FC Barcelona" in jugador["equipo"]]

print(barcelona_futbolistas)