from datos import jugadores

"""
Nombre: Daniel Santana Bueno
Ejercicio 02
Muestra la lista de los jugadores que llevan el dorsal número 10.
"""
dorsal10_futbolistas = [jugador for jugador in jugadores if jugador["dorsal"] == 10]

print(dorsal10_futbolistas)