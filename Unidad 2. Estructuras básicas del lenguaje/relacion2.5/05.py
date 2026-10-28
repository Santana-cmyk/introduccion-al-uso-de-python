from datos import series
'''
Nombre: Daniel Santana Bueno
Desc: Muestra una lista con los comentarios que tengan más de 40 caracteres.
'''

reseniasElena = [s["reseñas"] for s in series for resena in s["reseñas"] if (len(resena["comentario"])) > 40]

print(reseniasElena)

