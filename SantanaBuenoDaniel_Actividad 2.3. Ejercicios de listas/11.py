"""
Nombre: Daniel Santana Bueno

Desc:
Inserta al final de la lista un nuevo personaje que tenga todos los campos con algún
valor con sentido (puedes inventártelos, pero que sean razonables).
"""

from anexo2 import personajes_frieren

personaje_nuevo = {
    "nombre": "Erika",
    "raza": "Elfo",
    "clase": "Maga",
    "edad": 120,
    "afiliacion": ["Grupo de Frieren"],
}

personajes_frieren.append(personaje_nuevo)

