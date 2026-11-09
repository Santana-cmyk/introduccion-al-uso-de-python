from datos import series
'''
Nombre: Daniel Santana Bueno
Desc: Muestra una lista de tuplas (titulo_serie, comentario) para todas las reseñas que
hayan dado una puntuación de 10.
'''

seriesPuntuacion10 = [(s["titulo"], comentario["comentario"]) for s in series for comentario in s["reseñas"] if comentario["nota"] == 10]


print(seriesPuntuacion10)