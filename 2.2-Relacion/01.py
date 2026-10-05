"""
Nombre: Daniel Santana Bueno

Desc: 
Pedir al usuario un número entero y calcular el sumatorio desde 1 hasta dicho
número (incluido). Si el número introducido es menor que 1, mostrar un mensaje de
error.
"""

n = int(input("Ingrese un número entero: "))

if n < 1:
    print("Error: el número debe ser mayor o igual a 1.")
else:
    for i in range(1,n):
        print(i + (i+1))
