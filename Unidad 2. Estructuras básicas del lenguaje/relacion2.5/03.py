from datos import series
'''
Nombre: Daniel Santana Bueno
Desc: Muestra los títulos de las series que tengan una nota igual o superior a 9 y que 
además tengan 3 o más géneros. 

'''

seriesNota = [s["titulo"] for s in series if s["nota"] >= 9 and len(s["generos"]) >= 3]

print(seriesNota)