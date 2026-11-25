def resumir_marcadores(marcadores):
    resumen = {"victorias": 0, "empates": 0, "derrotas": 0,
               "puntos": 0, "diferencia": 0}
    for favor, contra in marcadores:
        resumen["diferencia"] += favor - contra
        if favor > contra:
            resumen["victorias"] += 1
            resumen["puntos"] += 3
        elif favor == contra:
            resumen["empates"] += 1
            resumen["puntos"] += 1
        else:
            resumen["derrotas"] += 1
    return resumen


if __name__ == "__main__":
    assert resumir_marcadores([(2, 0), (1, 1), (0, 3)]) == {"victorias": 1, "empates": 1, "derrotas": 1, "puntos": 4, "diferencia": -1}
    assert resumir_marcadores([]) == {"victorias": 0, "empates": 0, "derrotas": 0, "puntos": 0, "diferencia": 0}
