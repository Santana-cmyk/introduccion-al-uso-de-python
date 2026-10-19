"""
Nombre: Daniel Santana Bueno

Desc:
14. A todos los personajes que pertenezcan a la Asociación Continental de Magia,
quítales esa afiliación.
"""

from anexo2 import personajes_frieren

afiliacion_a_quitar = "Asociación Continental de Magia"

for personaje in personajes_frieren:
    if afiliacion_a_quitar in personaje["afiliacion"]:
        personaje["afiliacion"].remove(afiliacion_a_quitar)