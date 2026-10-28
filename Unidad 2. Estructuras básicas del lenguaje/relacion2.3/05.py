"""
Nombre: Daniel Santana Bueno

Desc:
Muestra los pokémons que tengan un tipo que acabe en “a”.
"""

from anexo1 import pokemons

print("Pokemons cuyo nombre termina con 'a'")
for pokemon in pokemons:
    if pokemon["tipo"].endswith("a"):
        print(pokemon)