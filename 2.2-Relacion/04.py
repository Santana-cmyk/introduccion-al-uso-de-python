"""
Nombre: Daniel Santana Bueno

Desc: 
Pedir al usuario un número entero y añadir los x primeros números de la serie de
fibonacci desde 0 a una lista. Mostrar dicha lista al acabar. Si el número introducido
es menor que 0, mostrar un mensaje de error.
""" 

n = int(input("Ingrese un número: "))
if n < 0:
        print("Error")
else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        print(fib)

