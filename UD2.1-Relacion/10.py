"""
Nombre: Daniel Santana Bueno

Desc: 
Pedir al usuario dos valores enteros y mostrar por pantalla todos los números primos
dentro de ese rango. Si el primer número es mayor que el primero se mostrará por
pantalla un mensaje de error.
"""


n1 = int (input("Ingrese numero: "))
limit = int (input("Ingrese numero: "))
es_primo = True

if n1 > limit: 
    print("Error")
else:
    for i in range(n1, limit + 1):
        es_primo = True
        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break
        if es_primo and i > 1:
            print(i)
