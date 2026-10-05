"""
Nombre: Daniel Santana Bueno

Desc: 
Pedir al usuario dos valores por pantalla: el precio de un producto (float) y el tipo de
IVA (General, Reducido, Superreducido). Calcular el precio final del producto fruto
de sumarle el IVA en función de su tipo. Realizar una versión con IF y otra con
MATCH.

"""

precio = float(input("Precio del producto: "))
tipo_iva = input("Tipo de IVA (General, Reducido, Superreducido): ")

if tipo_iva == "General":
    precio_final = precio * 1.21
elif tipo_iva == "Reducido":
    precio_final = precio * 1.10
elif tipo_iva == "Superreducido":
    precio_final = precio * 1.04


# Version con match
match tipo_iva: 
    case "General":
        precio_final = precio * 1.21
    case "Reducido": 
        precio_final = precio * 1.10
    case "Superreducido":
        precio_final = precio * 1.04
    case _: 
        print("Error")

print(precio_final, "€")

