from datos import series
'''
Nombre: Daniel Santana Bueno
Desc: Muestra una lista de tuplas (titulo_serie, nota_dada) de las reseñas dejadas por el 
usuario Elena.

'''

reseniasElena = [(s["titulo"], s["nota"]) for s in series for resena in s["reseñas"] if resena["usuario"] == "Elena"]

print(reseniasElena)

