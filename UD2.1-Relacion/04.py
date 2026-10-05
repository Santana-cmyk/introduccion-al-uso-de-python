"""
Nombre: Daniel Santana Bueno

Desc: 
A partir de 60 mm de lluvia acumulados en 12 horas se declara una alerta amarilla, y
a partir de 120 mm, una alerta roja. Pedir al usuario los milímetros de lluvia
acumulados y mostrar por pantalla si No hay alerta, Hay alerta amarilla o Hay
alerta roja. Realizar una versión con IF y otra con MATCH.
"""

# Versión con IF

milimetros = float(input("Milimetros de lluvia: "))

if milimetros >= 60 and milimetros < 120:
    print("Se declara alerta amarilla")
elif milimetros >= 120: 
    print("Se declara la alerta roja")
elif milimetros >= 0 and milimetros < 60:
    print("No se declara alerta")
else: 
    print("Error, valores negativos")

# Versión con MATCH

match milimetros:
    case n if n > 60 and n < 120:
        print("Se declara alerta amarilla") 
    case n if n >=120:
        print("Se declara alerta roja")
    case n if n >= 0 and n < 60:
        print("No se declara alerta")
    case _: 
        print("Error, valores negativos")