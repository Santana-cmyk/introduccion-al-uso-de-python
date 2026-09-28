"""
Nombre: Daniel Santana Bueno

Desc: 
Pedir al usuario una nota numérica entera mediante un input y diga si la calificación
es Suspenso, Aprobado, Notable, Sobresaliente, o No válida (en caso de que la
entrada sea diferente a la esperada). Realizar una versión con IF y otra con MATCH.
"""

nota = int(input("Ingrese un número: "))

# Version con IF

if nota >= 1 and nota <= 4:
    print("suspenso")
elif nota == 5: 
    print("Suficiente")
elif nota == 6:
    print("Bien")
elif nota >= 7 and nota <= 8:
    print("Notable")
elif nota >= 9 and nota <=10:
    print("Sobresaliente")
else: 
    print("Error nota inválida")


# Version con MATCH

match nota:
    case n if n >= 1 and n <= 4:
        print("suspenso")
    case 5: 
        print("Suficiente")
    case 6:
        print("Bien")
    case n if n >= 7 and n <= 8:
        print("Notable")
    case n if n >= 9 and n <=10:
        print("Sobresaliente")
    case _: 
        print("Error nota inválida")