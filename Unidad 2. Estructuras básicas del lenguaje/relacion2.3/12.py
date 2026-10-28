"""
Nombre: Daniel Santana Bueno

Desc:
Elimina todos los personajes cuya raza sea demonio.
"""

from anexo2 import personajes_frieren

for personaje in personajes_frieren[:]:
    if personaje["raza"] == "Demonio":
        personajes_frieren.remove(personaje)
