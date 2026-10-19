"""
Nombre: Daniel Santana Bueno

Desc:
Añádele a todos los elfos la afiliación “Elfos Supervivientes del Examen de Python”
"""

from anexo2 import personajes_frieren

afiliacion_nueva = "Elfos Supervivientes del Examen de Python"

for personaje in personajes_frieren:
    if personaje["raza"] == "Elfo" and afiliacion_nueva not in personaje["afiliacion"]:
        personaje["afiliacion"].append(afiliacion_nueva)
