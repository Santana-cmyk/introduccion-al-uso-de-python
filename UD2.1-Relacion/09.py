"""
Nombre: Daniel Santana Bueno

Desc: 
Pedir al usuario un número entero y mostrar por pantalla si el número es primo o no.
"""

numero = int (input("Ingrese numero: "))
es_primo = True

if numero <= 1:
    es_primo = False
else: 
    for  i in range(2,numero):
            if i % numero != 0:
                es_primo = True

if es_primo:
     print(numero, " es primo")
else:
     print(numero, " no es primo")
