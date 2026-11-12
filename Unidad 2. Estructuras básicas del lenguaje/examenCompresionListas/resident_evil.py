from datos import personajes


def ejercicio1():
    resultado1 = [p["nombre"]for p in personajes if p["afiliacion"] == "Policia de Raccoon City" and p["vivo"]]
    print(resultado1)


def ejercicio2():
    resultado2 = [p["nombre"] for p in personajes if p["afiliacion"] == "Policia de Raccoon City" and "Pistola Samurai Edge" in p["armas"] and "Lanzagranadas" in p["armas"]]
    print(resultado2)


def ejercicio3():
    resultado3 = [(p["nombre"], p["afiliacion"])for p in personajes if p["afiliacion"] != "Policia de Raccoon City"]
    print(resultado3)


def ejercicio4():
    resultado4 = [f'{p["nombre"]} ({p["afiliacion"]})'for p in personajes if p["registro_misiones"]["misiones_completadas"] >= 20]
    print(resultado4)


def ejercicio5():
    resultado5 = [(p["nombre"], p["estatura_m"] * 100)for p in personajes if p["estatura_m"] > 1.70]
    print(resultado5)


def ejercicio6():
    resultado6 = [p["armas"] for p in personajes]
    print(resultado6)


def ejercicio7():
    resultado7 = [p["nombre"] for p in personajes if p["registro_misiones"]["zombies_solo"] + p["registro_misiones"]["zombies_equipo"] >= 100]
    print(resultado7)


def ejercicio8():
    resultado8 = [{"nombre" : p["nombre"], "zombies_totales" : p["registro_misiones"]["zombies_solo"] + p["registro_misiones"]["zombies_equipo"]} for p in personajes]
    print(resultado8)



def ejercicio9():
    media = sum([p["estatura_m"] for p in personajes]) / len(personajes)
    print(media)


def ejercicio10():
    media = sum([p["estatura_m"] for p in personajes]) / len(personajes)
    resultado10 = [(p["nombre"], p["estatura_m"]) for p in personajes if p["estatura_m"] > media]
    print(resultado10)
    