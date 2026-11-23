animales = [
    ["Lobo ibérico", "Mamífero", 2500],
    ["Lince ibérico", "Mamífero", 1668],
    ["Quebrantahuesos", "Ave", 2000],
    ["Oso pardo", "Mamífero", 500],
]


def comprobar_estado(nombre: str):
    for animal in animales:
        poblacion = animal[2]

        if nombre not in animal[0]:
            raise ValueError("Nombre no encontrado")
        elif poblacion == 0:
            return "Extinto"
        elif poblacion > 0 and poblacion <= 500:
            return "En peligro crítico"
        elif poblacion > 500 and poblacion <= 2000:
            return "En peligro"
        elif poblacion > 2000:
            return "Amenazado"
