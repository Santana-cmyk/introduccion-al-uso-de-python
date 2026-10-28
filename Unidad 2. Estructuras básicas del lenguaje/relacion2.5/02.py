from datos import series
'''
Nombre: Daniel Santana Bueno
Desc: Muestra los títulos de las series que sean de Fantasía o Misterio. 

'''
seriesFantasiaMisterio = [s["titulo"] for s in series if "Fantasía" in s["generos"] or "Misterio" in s["generos"]]

print(seriesFantasiaMisterio)