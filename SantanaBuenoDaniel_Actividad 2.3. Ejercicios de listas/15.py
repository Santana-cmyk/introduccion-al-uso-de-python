"""
Nombre: Daniel Santana Bueno

Desc:
Modifica la raza de todos los humanos que tengan 100 o más años a “Zombie”.

"""

from anexo2 import personajes_frieren

for personaje in personajes_frieren:
    if personaje["raza"] == "Humano" and personaje["edad"] >= 100:
        personaje["raza"] = "Zombie"
