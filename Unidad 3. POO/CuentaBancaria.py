class CuentaBancaria:
    def __init__(self, nombre: str, saldo: float = 0):
        if saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self.nombre = nombre
        self.saldo = saldo

    def ingresar (self, cantidad : float):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.saldo += cantidad

    def retirar (self, cantidad : float):
        if cantidad < 0: 
            raise ValueError("La cantidad no puede ser negativa o superior al saldo")
        self.saldo -= cantidad

    def __str__(self):
        return f"Cuenta Bancaria: [Nombre = {self.nombre} | Saldo = {self.saldo}] "

cuenta1 = CuentaBancaria("Pepito")
cuenta2 = CuentaBancaria("Juanito", 1000)
cuenta1.ingresar(500)
cuenta2.ingresar(750)
print(cuenta1)
print(cuenta2)