from datos import series
'''
Nombre: Daniel Santana Bueno
Desc: Muestra una lista con todos los géneros de todas las series. No importa si hay
géneros duplicados.
'''

generos = [s["generos"] for s in series]

print(generos)
