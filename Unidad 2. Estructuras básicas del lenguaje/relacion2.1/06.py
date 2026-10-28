"""
Nombre: Daniel Santana Bueno

Desc: 
Supongamos que la contraseña para acceder es “12345”. Pedir al usuario la
contraseña por pantalla y, si es la correcta, mostrar un mensaje de bienvenida. Si la
contraseña introducida es incorrecta, volver a pedirla hasta que se introduzca
correctamente.

"""

password = "12345"

contraseña = input("Introduce la contraseña: ")

while contraseña != password:
    print("Contraseña incorrecta. Inténtalo de nuevo.")
    contraseña = input("Introduce la contraseña: ")

print("Bienvenido.")