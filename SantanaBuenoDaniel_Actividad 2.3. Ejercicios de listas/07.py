"""
Nombre: Daniel Santana Bueno

Desc:
Elimina todos los pokémons de tipo normal.
"""
from anexo1 import pokemons

print("Pokemons de tipo normal a eliminar: ")
for pokemon in pokemons[:]:
    if "Normal" in pokemon["tipos"]:
        print(pokemon)
        pokemons.remove(pokemon)