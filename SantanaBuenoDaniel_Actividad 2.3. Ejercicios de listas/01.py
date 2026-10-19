"""
Nombre: Daniel Santana Bueno

Desc:
Dada la lista del Anexo I, realiza los siguientes ejercicios de listas:
"""
from anexo1 import pokemons

# 1. Muestra en una sóla línea el nombre y el peso del pokémon con más peso.
mayor = 0

for pokemon in pokemons:
    if pokemon["peso_kg"] > mayor:
        mayor = pokemon["peso_kg"]
        nombre_mayor = pokemon["nombre"]
    
print(nombre_mayor, mayor , "kg")
