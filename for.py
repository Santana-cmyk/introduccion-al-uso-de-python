# numero = int(input("Ingrese un número: "))

# if numero > 0:
#     print("El número es positivo.")
# elif numero < 0: 
#     print("negativo")
# else:
#     print("cero")

# dia = input("Introduce un dia: ")

# match dia: 
#     case "lunes":
#         print("Hay clase")
#     case "martes":
#         print("No hay clase")
#     case _:
#         print("Error")

# match numero:
#     case n if n < 0:
#         print("Negativo")
#     case n if n > 0:
#         print("Positivo")
#     case _: 
#         print("Cero")

# if dia == "lunes" or dia == "miercoles":
#     print("Hay clase")
# elif dia == "martes" or dia == "jueves" or dia == "viernes":
#     print("No hay clase")
# else: 
#     print("Error3")

# peliculas = [
#     { "titulo" : "Resident Evil", "nota" : 6.5},
#     { "titulo" : "Robocop", "nota" : 8.5},
#     { "titulo" : "Terminator", "nota" : 9},
# ]

# for pelicula in peliculas:
#     if pelicula["nota"] >= 7:
#         print(pelicula["titulo"])

texto = "Hola mundo"

for letra in texto:
    print(letra)