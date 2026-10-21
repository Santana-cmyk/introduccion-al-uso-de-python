# ANEXO I: lista de películas
peliculas = [
    {
        "titulo": "Inception",
        "duracion": 148,
        "año_estreno": 2010,
        "edad_recomendada": 13,
        "generos": ["Ciencia ficción", "Acción", "Intriga"]
    },
    {
        "titulo": "El Viaje de Chihiro",
        "duracion": 125,
        "año_estreno": 2001,
        "edad_recomendada": 7,
        "generos": ["Animación", "Fantasía", "Aventura"]
    },
    {
        "titulo": "El Padrino",
        "duracion": 175,
        "año_estreno": 1972,
        "edad_recomendada": 18,
        "generos": ["Crimen", "Drama"]
    },
    {
        "titulo": "Toy Story",
        "duracion": 81,
        "año_estreno": 1995,
        "edad_recomendada": 0,  # Apta para todos los públicos
        "generos": ["Animación", "Comedia", "Aventura"]
    },
    {
        "titulo": "Interstellar",
        "duracion": 169,
        "año_estreno": 2014,
        "edad_recomendada": 12,
        "generos": ["Ciencia ficción", "Drama", "Aventura"]
    },
    {
        "titulo": "Parásitos",
        "duracion": 132,
        "año_estreno": 2019,
        "edad_recomendada": 16,
        "generos": ["Drama", "Thriller", "Comedia negra"]
    },
    {
        "titulo": "El Señor de los Anillos: La Comunidad del Anillo",
        "duracion": 178,
        "año_estreno": 2001,
        "edad_recomendada": 12,
        "generos": ["Fantasía", "Aventura", "Acción"]
    },
    {
        "titulo": "Pulp Fiction",
        "duracion": 154,
        "año_estreno": 1994,
        "edad_recomendada": 18,
        "generos": ["Crimen", "Drama"]
    },
    {
        "titulo": "Coco",
        "duracion": 105,
        "año_estreno": 2017,
        "edad_recomendada": 0,
        "generos": ["Animación", "Familia", "Fantasía"]
    },
    {
        "titulo": "Matrix",
        "duracion": 136,
        "año_estreno": 1999,
        "edad_recomendada": 16,
        "generos": ["Ciencia ficción", "Acción"]
    }
]

# Lista del ejercicio 7. Se declara aquí (fuera de las funciones) para que
# siga existiendo cuando el ejercicio 8 borre películas de 'peliculas'.
peliculas_infantiles = []


def ejercicio1():
    # EJERCICIO 1: añadir una película con todos sus datos completos.
    nueva_pelicula = {
        "titulo": "Harry Potter y la piedra filosofal",
        "duracion": 152,
        "año_estreno": 2001,
        "edad_recomendada": 7,
        "generos": ["Fantasía", "Aventura", "Familia"]
    }
    # append() añade el diccionario al final de la lista
    peliculas.append(nueva_pelicula)


def ejercicio2():
    # EJERCICIO 2: mostrar título y duración de las películas que duran
    # más que la media.

    # Paso 1: sumar las duraciones de todas las películas
    suma_duracion = 0
    for pelicula in peliculas:
        suma_duracion += pelicula["duracion"]

    # Paso 2: media = suma / número de películas
    media = suma_duracion / len(peliculas)

    # Paso 3: imprimir las que superan la media con formato "titulo duracion"
    for pelicula in peliculas:
        if pelicula["duracion"] > media:
            print(pelicula["titulo"], pelicula["duracion"])


def ejercicio3():
    # EJERCICIO 3: a las películas de género Drama, cambiarles la edad
    # recomendada a 18.
    for pelicula in peliculas:
        # 'in' comprueba si "Drama" está dentro de la lista de géneros
        if "Drama" in pelicula["generos"]:
            # Al modificar el diccionario, se modifica la lista original
            pelicula["edad_recomendada"] = 18


def ejercicio4():
    # EJERCICIO 4: mostrar título y duración de las películas que sean de
    # Fantasía y Aventura al mismo tiempo (ambos géneros a la vez).
    for pelicula in peliculas:
        if "Fantasía" in pelicula["generos"] and "Aventura" in pelicula["generos"]:
            print(pelicula["titulo"], pelicula["duracion"])


def ejercicio5():
    # EJERCICIO 5: mostrar título y edad recomendada de las películas cuya
    # edad esté entre 7 y 13 (ambos incluidos).
    # Formato: "titulo edad_recomendada"
    for pelicula in peliculas:
        if pelicula["edad_recomendada"] >= 7 and pelicula["edad_recomendada"] <=13:
            print(pelicula["titulo"], pelicula["edad_recomendada"])


def ejercicio6():
    # EJERCICIO 6: añadir el género "Infantil" a las películas cuya edad
    # recomendada sea 0.
    for pelicula in peliculas:
        if pelicula["edad_recomendada"] == 0:
            # 'generos' es una lista, así que usamos append()
            pelicula["generos"].append("Infantil")


def ejercicio7():
    # EJERCICIO 7: crear una copia de la lista llamada peliculas_infantiles
    # que contenga solo las películas con el género "Infantil".

    # Paso 1: copiamos la lista (copy() crea una lista nueva, independiente
    # de 'peliculas', de modo que borrar de una no afecta a la otra)
    copia = peliculas.copy()

    # Paso 2: nos quedamos solo con las que tienen el género "Infantil".
    # Con [:] = ... se modifica la lista global en vez de crear una local.
    peliculas_infantiles[:] = [p for p in copia if "Infantil" in p["generos"]]


def ejercicio8():
    # EJERCICIO 8: borrar todas las películas cuya edad recomendada sea 0.

    # No se debe borrar elementos de una lista mientras se recorre con un
    # for (se saltarían elementos). Por eso construimos una lista nueva solo
    # con las películas que NO tienen edad 0 y sustituimos el contenido de la
    # lista original con [:] = ...
    for pelicula in peliculas[:]:
        if pelicula["edad_recomendada"] == 0:
            peliculas.remove(pelicula)

def main():
    ejercicio1()
    ejercicio2()
    ejercicio3()
    ejercicio4()
    ejercicio5()
    ejercicio6()
    ejercicio7()
    ejercicio8()


if __name__ == '__main__':
    main()
