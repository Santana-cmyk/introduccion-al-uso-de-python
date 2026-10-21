from datos import personajes

# Nombre: Daniel Santana Bueno


def ejercicio1():

    personajeNuevo = {
        "nombre": "Rengoku",
        "raza": "Humano",
        "ocupacion": "Cazador de demonios",
        "estilo_combate": ["Respiración fuego"],
        "atributos": {"fuerza": 89, "defensa": 90, "velocidad": 80},
    }
    personajes.append(personajeNuevo)


def ejercicio2():
    for personaje in personajes:
        atributos = personaje["atributos"]
        media = (atributos["fuerza"] + atributos["defensa"] + atributos["velocidad"]) / 3
        if media > 85:
            print(personaje)


def ejercicio3():
    sumaFuerza = 0
    for personaje in personajes:
        sumaFuerza += personaje["atributos"]["fuerza"]

    media_fuerza = sumaFuerza / len(personajes)

    for personaje in personajes:
        if personaje["atributos"]["fuerza"] > media_fuerza:
            print(personaje)


def ejercicio4():
    for personaje in personajes:
        if "Respiración del Agua" in personaje["estilo_combate"]:
            nuevaFuerza = personaje["atributos"]["fuerza"] + 10
            if nuevaFuerza > 100:
                nuevaFuerza = 100
            personaje["atributos"]["fuerza"] = nuevaFuerza

    for personaje in personajes:
        print(personaje["nombre"], personaje["atributos"]["fuerza"])


def ejercicio5():
    zenitsu = ""
    for personaje in personajes:
        if personaje["nombre"] == "Zenitsu Agatsuma":
            zenitsu = personaje

    zenitsuFuerza = zenitsu["atributos"]["fuerza"]
    for personaje in personajes:
        if personaje["nombre"] != "Zenitsu Agatsuma":
            if zenitsuFuerza > personaje["atributos"]["defensa"]:
                print(personaje["nombre"] , personaje["atributos"]["fuerza"], personaje["atributos"]["defensa"])


def ejercicio6():
    for personaje in personajes[:]:
        if personaje["ocupacion"] == "Cazador de demonios":
            personajes.remove(personaje)
    print(personajes)
