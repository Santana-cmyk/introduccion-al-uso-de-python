from Figura import Figura

class Circulo(Figura):
    def __init__(self, radio = 3, diametro = 13, circunferencia = 20):
        if radio < 0 or diametro < 0 or circunferencia < 0:
            raise ValueError("Los valores de radio, diámetro y circunferencia no deben ser negativos.")

        self.radio = radio
        self.diametro = diametro
        self.circunferencia = circunferencia

    def area(self):
        return 3.14 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.radio

    def __str__(self):
        return f"Circulo [Radio = {self.radio} | Diametro = {self.diametro} | Circunferencia = {self.circunferencia}]"