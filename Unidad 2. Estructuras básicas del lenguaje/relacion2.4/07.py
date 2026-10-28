from datos import jugadores

"""
Nombre: Daniel Santana Bueno
Ejercicio 07
Crea una lista de cadenas de texto con la forma "Nombre (Equipo)" para cada
jugador. Muéstrala.
"""

jugadores_ruleta = [
    f'{jugador["nombre"]} ({jugador["equipo"]})'
    for jugador in jugadores
]

print(jugadores_ruleta)
