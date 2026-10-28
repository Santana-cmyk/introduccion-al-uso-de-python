from datos import jugadores

"""
Nombre: Daniel Santana Bueno
Ejercicio 10
Extrae en una única lista todas las filigranas de todos los jugadores (no importa si
hay duplicadas) y muéstrala.
"""

filigranas = [
    filigrana
    for jugador in jugadores
    for filigrana in jugador["filigranas"]
]

print(filigranas)
