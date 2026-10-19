"""
Nombre: Daniel Santana Bueno

Desc:
Muestra el nombre, la raza y la edad de los personajes del grupo de los cuatro
héroes.
"""

from anexo2 import personajes_frieren

for personaje in personajes_frieren:
    for afiliacion in personaje["afiliacion"]:
        if afiliacion == "Grupo de los Cuatro Héroes":
            print(personaje["nombre"], personaje["raza"])
