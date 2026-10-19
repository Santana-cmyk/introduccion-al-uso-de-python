"""
Nombre: Daniel Santana Bueno

Desc:
Muestra la edad media de los personajes humanos.
"""

from anexo2 import personajes_frieren

print("Edad media de los personajes humanos")

suma_edades = 0
num_humanos = 0

for personaje in personajes_frieren:
    if personaje["raza"] == "Humano":
        suma_edades += personaje["edad"]
        num_humanos += 1
        
media = suma_edades / num_humanos
print(media)
