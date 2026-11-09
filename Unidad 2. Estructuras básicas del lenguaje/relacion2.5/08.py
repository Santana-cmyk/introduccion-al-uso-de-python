from datos import series
'''
Nombre: Daniel Santana Bueno
Muestra una lista de tuplas que incluya el título de la serie y “Obra maestra” si las
notas medias dadas en las reseñas es igual o superior a 9, y “Gran serie” en caso
contrario.
'''

seriesPuntuacionMedia = [
    (
        s["titulo"],
        "Obra maestra" if (sum(n["nota"] for n in s["reseñas"]) / len(s["reseñas"]) >= 9) else "Gran serie"
    )
    for s in series
    
]


print(seriesPuntuacionMedia)