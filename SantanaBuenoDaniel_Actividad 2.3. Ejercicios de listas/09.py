"""
Nombre: Daniel Santana Bueno

Desc:
Muestra el nombre y la raza de todos los personajes que sean magos de primera
clase.
"""

from anexo2 import personajes_frieren

print("Magos en el grupo")

for personaje in personajes_frieren:
    for afiliacion in personaje["afiliacion"]:
        if afiliacion == "Magos de Primera Clase":
            print(personaje["nombre"], personaje["raza"])