from datos import series
'''
Nombre: Daniel Santana Bueno
Desc: Muestra una lista de cadenas con el formato 
"La seria (titulo) tiene n reseñas, para todas las seriess
'''
seriesResenas = [f"La series {s['titulo']} tiene {len(s['reseñas'])} reseñas" for s in series]

print(seriesResenas)

