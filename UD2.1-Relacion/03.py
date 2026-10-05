"""
Nombre: Daniel Santana Bueno

Desc: 
Pedir al usuario la edad de una persona y mostrar si es mayor o menor de edad. Si
la edad es menor a 0 mostrar un mensaje de error, y si es superior a 120 indicar que
es un vampiro.
"""

edad = int(input("Introduce tu edad: "))

if edad >= 18: 
    print("Eres mayor de edad")
    if edad >= 120:
        print("Eres un vampiro")
elif edad < 18 and edad > 0:
    print("Eres menor de edad")
else: 
    print("Error")
