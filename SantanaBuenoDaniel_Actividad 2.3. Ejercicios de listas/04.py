"""
Nombre: Daniel Santana Bueno

Desc:
Muestra el nombre y los tipos de los pokémons que sean de tipo agua.
"""
from anexo1 import pokemons
print("Pokemons de tipo agua:")
for pokemon in pokemons:
    if "Agua" in pokemon["tipos"]:
        print(pokemon["nombre"], ",", pokemon["tipos"])