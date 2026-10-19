"""
Nombre: Daniel Santana Bueno

Desc:
Dada la lista del Anexo I, realiza los siguientes ejercicios de listas:
Muestra la media de altura de todos los pokémons.
"""
from anexo1 import pokemons

suma = 0

for pokemon in pokemons:
    suma += pokemon["altura_m"]

media = suma / len(pokemons)

print(media)
