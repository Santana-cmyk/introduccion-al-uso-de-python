"""
Nombre: Daniel Santana Bueno

Desc:
Muestra el nombre y la altura de todos los pokémons que midan menos que la
media.
"""
from anexo1 import pokemons


suma = 0

for pokemon in pokemons:
    suma += pokemon["altura_m"]

media = suma / len(pokemons)

print("Pokemons que miden menos de la media")
for pokemon in pokemons:
    if pokemon["altura_m"] < media:
        print(pokemon["nombre"], ", ", pokemon["altura_m"])
