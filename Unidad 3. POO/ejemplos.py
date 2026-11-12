def sumatorio(numero : int) -> int:
    sumatorio = 0
    for i in range(1,numero+1):
        sumatorio += 1
    return sumatorio

def suma(*numeros):
    return sum(numeros)

print(suma(1,2,3,4))

def suma2(a,b):
    return a+b, a, b

a , b, c = suma2(1,2)
print(a,b,c)