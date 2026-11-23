from abc import ABC, abstractclassmethod

class Figura(ABC):
    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def perimetro(self):
        pass