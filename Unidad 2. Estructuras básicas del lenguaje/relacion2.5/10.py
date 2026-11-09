from datos import series
'''
Nombre: Daniel Santana Bueno
Desc: 10. Muestra una lista con todos los nombres de los usuarios que hayan opinado en
alguna serie de Drama. No importa si hay nombres repetidos.
'''

usuariosDrama = [reseña["usuario"] for s in series
                 if "Drama" in s["generos"]
                 for reseña in s["reseñas"]]
print(usuariosDrama)