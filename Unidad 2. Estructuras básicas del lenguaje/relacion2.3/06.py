"""
Nombre: Daniel Santana Bueno

Desc:
Crea un nuevo Pokémon en una variable, añádelo al final de la lista y muestra
el valor asociado al tipo Agua.
"""

from anexo1 import pokemons

nuevo_pokemon = {
    "nombre": "Palkia",
    "generacion": 4,
    "categoria": "Espacial",
    "tipos": {"Agua": 660, "Dragon": 63},
    "peso_kg": 336.0,
    "altura_m": 4.2,
}

pokemons.append(nuevo_pokemon)
print(pokemons[-1]["tipos"]["Agua"])
