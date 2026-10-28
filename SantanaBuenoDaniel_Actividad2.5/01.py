from datos import series
'''
Nombre: Daniel Santana Bueno
Desc: Muestra una lista con los títulos de las series que sean de Animación.

'''

seriesAnimacion = [s["titulo"] for s in series if "Animación" in s["generos"]]

print(seriesAnimacion)