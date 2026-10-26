from datos import jugadores

"""
Nombre: Daniel Santana Bueno
Ejercicio 01
Muestra una lista solo con los nombres de todos los futbolistas.
"""

nombres_futbolistas = [j["nombre"] for j in jugadores]

print(nombres_futbolistas)
