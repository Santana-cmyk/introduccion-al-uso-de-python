from datos import personajes


def ejercicio_1():
    # (1 punto). Muestra una lista con los nombres de los personajes afiliados al Cuerpo
    # de Exploración que estén vivos.
    resultado = [
        p["nombre"]
        for p in personajes
        if p["afiliacion"] == "Cuerpo de Exploración" and p["vivo"]
    ]
    print("Ejercicio 1:", resultado)


def ejercicio_2():
    # (1 punto). Muestra los nombres de los personajes afiliados al Cuerpo de
    # Exploración que tengan las habilidades Supervivencia y Sigilo.
    resultado = [
        p["nombre"]
        for p in personajes
        if p["afiliacion"] == "Cuerpo de Exploración"
        and "Supervivencia" in p["habilidades"]
        and "Sigilo" in p["habilidades"]
    ]
    print("Ejercicio 2:", resultado)


def ejercicio_3():
    # (1 punto). Muestra una lista de tuplas con el nombre y la afiliación de todos los
    # personajes que no pertenezcan al Cuerpo de Exploración.
    resultado = [
        (p["nombre"], p["afiliacion"])
        for p in personajes
        if p["afiliacion"] != "Cuerpo de Exploración"
    ]
    print("Ejercicio 3:", resultado)


def ejercicio_4():
    # (1 punto). Muestra una lista de cadenas de caracteres que incluya el nombre del
    # personaje seguido de un espacio en blanco y su afiliación entre paréntesis, para
    # todos los personajes que hayan completado 20 misiones o más.
    resultado = [
        f'{p["nombre"]} ({p["afiliacion"]})'
        for p in personajes
        if p["registro_combate"]["misiones_completadas"] >= 20
    ]
    print("Ejercicio 4:", resultado)


def ejercicio_5():
    # (1 punto). Muestra una lista de tuplas con los nombres y las alturas en centímetros
    # de todos los personajes que midan más de 1,70 metros.
    resultado = [
        (p["nombre"], p["estatura_m"] * 100)
        for p in personajes
        if p["estatura_m"] > 1.70
    ]
    print("Ejercicio 5:", resultado)


def ejercicio_6():
    # (1 punto). Muestra una lista aplanada con todas las habilidades de todos los
    # personajes. No importa si hay habilidades repetidas.
    resultado = [habilidad for p in personajes for habilidad in p["habilidades"]]
    print("Ejercicio 6:", resultado)


def ejercicio_7():
    # (1 punto). Los atributos titanes_solo y titanes_equipo del registro de combate
    # indican la cantidad de titanes que ha matado el personaje en solitario o junto a su
    # equipo, respectivamente. Muestra una lista con los nombres de los personajes que
    # hayan matado 5 o más titanes en total.
    resultado = [
        p["nombre"]
        for p in personajes
        if p["registro_combate"]["titanes_solo"]
        + p["registro_combate"]["titanes_equipo"]
        >= 5
    ]
    print("Ejercicio 7:", resultado)


def ejercicio_8():
    # (1 punto). Muestra una lista de diccionarios con los atributos nombre y
    # titanes_totales, donde se muestre el nombre y el número de titanes que ha matado
    # cada personaje en total.
    resultado = [
        {
            "nombre": p["nombre"],
            "titanes_totales": p["registro_combate"]["titanes_solo"]
            + p["registro_combate"]["titanes_equipo"],
        }
        for p in personajes
    ]
    print("Ejercicio 8:", resultado)


def ejercicio_9():
    # (1 punto). La función sum nos permite sumar los valores de una lista. Calcula con
    # una comprensión de listas la media de las alturas de todos los personajes y
    # muéstrala.
    media = sum([p["estatura_m"] for p in personajes]) / len(personajes)
    print("Ejercicio 9:", media)


def ejercicio_10():
    # (1 punto). Calcula en una comprensión de listas la media de las alturas de todos los
    # personajes y luego en otra comprensión de listas muestra una lista de tuplas con los
    # nombres y las alturas de los personajes que midan más de la media. Muestra
    # únicamente la lista de tuplas resultante.
    media = sum([p["estatura_m"] for p in personajes]) / len(personajes)

    resultado = [
        (p["nombre"], p["estatura_m"]) for p in personajes if p["estatura_m"] > media
    ]
    print("Ejercicio 10:", resultado)
