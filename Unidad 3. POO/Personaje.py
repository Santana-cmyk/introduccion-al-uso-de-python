class Personaje:
    def __init__(self, vida: int, ataque: int):
        if vida <= 0 or ataque <= 0:
            raise ValueError("La vida y el ataque debe ser superiores a cero")
        self.vida = vida
        self.ataque = ataque

    def recibir_dano(self, cantidad: int):
        self.vida = max(0, self.vida - cantidad)

    def atacar(self, objetivo: Personaje):
        objetivo.recibir_dano(self.ataque)


class Guerrero(Personaje):
    def atacar(self, objetivo: Personaje):
        objetivo.recibir_dano(self.ataque * 2)


class Mago(Personaje):
    def __init__(self, vida, ataque: int, mana: int):
        super().__init__(vida, ataque)
        self.mana = mana

    def atacar(self, objetivo: Personaje):
        # El mago solo puede atacar con magia si tiene 5 o  más de mana
        # Si tiene maná, triplica su ataque

        if self.mana > 5:
            objetivo.recibir_dano(self.ataque * 3)
            self.mana -= 5
        else:
            objetivo.recibir_dano(self.ataque)


goku = Guerrero(100, 20)
ryu = Personaje(80, 30)

goku.atacar(ryu)
ryu.atacar(goku)
print(goku.vida)
print(ryu.vida)
