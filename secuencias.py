PI = 3.14
print(PI)


# SECUENCIAS

# LISTAS

lista = [1,2,3]
print(lista)
print("Primero:", lista[0])
print("ultimo:", lista[-1])
lista[-1] = "Patata"
print(lista[-1])

producto = [142, "TV LG 40 pulgadas", 399.95]
print(producto)

listaA = ["A","B"]
listaB = ["C","D"]
listaA.extend(listaB)
listaA.extend(["E","F"])
print(listaA)
listaA.append("G")
print(listaA)
del listaA[0]
print(listaA)

# TUPLAS - "Arrays constantes"

tupla = (1,2,3)
print(tupla)

# RANGOS

rango = range(1,10)
print(rango[4])

# input siempre detectará el valor por un string, hay que CASTEAR al tipo de valor deseado.
inicio = int(input("Inicio: "))
final = int(input("Final: "))
rango = range(inicio, final)
print(rango[2])

# DICCIONARIO

# clave-valor
diccionario = {
    "titulo" : "Crash Bandicoot",
    "consola" : "PSX",
    "Precio" : 59.95
}

print(diccionario)
print(diccionario["titulo"])
print(diccionario["consola"])
print(diccionario["Precio"])
