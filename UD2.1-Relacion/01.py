"""
Nombre: Daniel Santana Bueno

Desc: 
Pedir al usuario una nota numérica entera mediante un input y diga si la calificación
es Suspenso, Aprobado, Notable, Sobresaliente, o No válida (en caso de que la
entrada sea diferente a la esperada). Realizar una versión con IF y otra con MATCH.
"""

numero = int(input("Ingrese un número: "))

if numero >= 1 and numero <= 4:
    print("suspenso")
elif numero == 5: 
    print("Suficiente")
elif numero == 6:
    print("Bien")
elif numero >= 7 and numero <= 8:
    print("Notable")
elif numero >= 9 and numero <=10:
    print("Sobresaliente")
else: 
    print("Error nota inválida")