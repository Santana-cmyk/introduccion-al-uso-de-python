"""
Nombre: Daniel Santana Bueno

Desc:
Inserta al final de la lista un nuevo pokémon que tenga todos los campos con algún
valor con sentido (puedes inventártelos, pero que sean razonables).
"""

from anexo1 import pokemons

pokemons.append(
    {
        "nombre": "Palkia",
        "generacion": 4,
        "categoria": "Espacial",
        "tipos": ["Agua", "Dragon"],
        "peso_kg": 336.0,
        "altura_m": 4.2,
    }
)
