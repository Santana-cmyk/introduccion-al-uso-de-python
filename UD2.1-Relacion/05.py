"""
Nombre: Daniel Santana Bueno

Desc: 
Pedir al usuario dos números enteros y mostrar los números pares dentro de dicho
intervalo. Si el primer número es mayor que el primero se mostrará por pantalla un
mensaje de error. Realizar una versión con FOR y otra con WHILE.
"""

n1 = int(input("1º número: "))
n2 = int(input("2º número: "))

if n1 > n2:
    print("Error: el primer número es mayor que el segundo.")
else:
    print("Número pares entre", n1, "y", n2, "con FOR:")
    for i in range(n1, n2 + 1):
        if i%2 == 0:
            print(i)

if n1 > n2:
    print("Error: el primer número es mayor que el segundo.")
else:
    print("Número pares entre", n1, "y", n2, "con WHILE:")
    i = n1
    while i <= n2:
        if i%2 == 0:
            print(i)
        i += 1