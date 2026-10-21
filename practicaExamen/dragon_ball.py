from datos import personajes


def ejercicio1():
    # EJERCICIO 1: añadir un nuevo personaje a la lista.
    # Un personaje es un diccionario con las 5 claves del enunciado:
    # nombre y raza (str), nivel_pelea (int), tecnicas (lista de str)
    # y atributos (diccionario con fuerza, defensa y velocidad <= 100).
    nuevo_personaje = {
        "nombre": "Trunks",
        "raza": "Saiyan",
        "nivel_pelea": 100000000,
        "tecnicas": ["Espada Ki", "Burning Attack", "Big Bang Attack"],
        "atributos": {"fuerza": 88, "defensa": 80, "velocidad": 85},
    }
    # append() añade el diccionario al final de la lista 'personajes'
    personajes.append(nuevo_personaje)


def ejercicio2():
    # EJERCICIO 2: mostrar los personajes cuya media de fuerza, defensa
    # y velocidad sea superior a 80.
    for personaje in personajes:
        # Guardamos el diccionario interno para no repetir personaje["atributos"]
        atributos = personaje["atributos"]
        # La media es la suma de los tres valores dividida entre 3
        media = (
            atributos["fuerza"] + atributos["defensa"] + atributos["velocidad"]
        ) / 3
        # Si supera 80, imprimimos el personaje entero (sin darle formato)
        if media > 80:
            print(personaje)


def ejercicio3():
    # EJERCICIO 3: mostrar los personajes cuya velocidad esté por encima
    # de la media de velocidad de todos los personajes.

    # Paso 1: sumar la velocidad de todos los personajes
    suma_velocidad = 0
    for personaje in personajes:
        suma_velocidad += personaje["atributos"]["velocidad"]

    # Paso 2: calcular la media (suma / número de personajes)
    media_velocidad = suma_velocidad / len(personajes)

    # Paso 3: volver a recorrer la lista e imprimir los que superan la media
    for personaje in personajes:
        if personaje["atributos"]["velocidad"] > media_velocidad:
            print(personaje)


def ejercicio4():
    # EJERCICIO 4: a los personajes con la técnica "Big Bang Attack" se les
    # suma 10 a la fuerza, sin que el valor supere 100.

    for personaje in personajes:
        # 'in' comprueba si la técnica está dentro de la lista de técnicas
        if "Big Bang Attack" in personaje["tecnicas"]:
            nueva_fuerza = personaje["atributos"]["fuerza"] + 10
            # Si nos pasamos de 100, lo dejamos en 100 (límite del enunciado)
            if nueva_fuerza > 100:
                nueva_fuerza = 100
            # Modificamos el valor directamente en la lista original
            personaje["atributos"]["fuerza"] = nueva_fuerza

    # Una vez modificada la lista, imprimimos nombre y fuerza de TODOS
    # los personajes con el formato pedido, por ejemplo: Goku 95
    for personaje in personajes:
        print(personaje["nombre"], personaje["atributos"]["fuerza"])


def ejercicio5():
    # Paso 1: Buscar a Vegeta de forma eficiente
    vegeta = None
    for personaje in personajes:
        if personaje["nombre"] == "Vegeta":
            vegeta = personaje
            break  # Rompemos el bucle: ya lo encontramos, no hace falta seguir buscando

    # Si no se encuentra a Vegeta, avisamos y salimos de la función para evitar que el programa falle
    if vegeta is None:
        print("Vegeta no se encuentra en la lista de personajes.")
        return

    # Paso 2: Comparar e imprimir
    fuerza_vegeta = vegeta["atributos"]["fuerza"]
    for personaje in personajes:
        if personaje["nombre"] != "Vegeta":
            if fuerza_vegeta > personaje["atributos"]["defensa"]:
                print(personaje["nombre"], personaje["atributos"]["defensa"])


def ejercicio6():
    # Recorremos una COPIA de la lista (personajes.copy()) y borramos de la
    # original. Si recorriéramos la original mientras borramos, se saltarían
    # elementos.
    for personaje in personajes[:]:
        if personaje["raza"] == "Cazador de demonios":
            personajes.remove(personaje)

    print(personajes)