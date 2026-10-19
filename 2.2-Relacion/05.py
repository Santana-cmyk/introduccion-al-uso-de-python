"""
Nombre: Daniel Santana Bueno

Desc:
Pedir al usuario un número y mostrar el triángulo de Pascal de ese número de filas.
En caso de que el número sea inferior a 1, mostrar un mensaje de error.
"""
    
num = int(input("Introduce el número de filas: "))

# Validación de error
if num < 1:
    print("Error: El número debe ser igual o superior a 1.")
else:
    fila = [1]
    
    # Bucle para generar y mostrar cada fila
    for i in range(num):
        # Mostrar la fila actual centrada
        espacios = " " * (num - i - 1)
        print(espacios + " ".join(map(str, fila)))
        
        # Calcular la siguiente fila basada en la actual
        nueva_fila = [1]
        for j in range(len(fila) - 1):
            nueva_fila.append(fila[j] + fila[j+1])
        nueva_fila.append(1)
        
        fila = nueva_fila