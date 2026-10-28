"""
Nombre: Daniel Santana Bueno

Desc: 
Pedir al usuario un número entero y calcular el factorial desde 1 hasta dicho número
(incluido). Si el número introducido es menor que 1, mostrar un mensaje de error.
"""
factorial = 1
n = int(input("Ingrese un número entero: "))

if n < 1:
    print("Error")
else:
    for i in range(1,n + 1):
           factorial *= i
           i = i + 1
           
print(factorial)