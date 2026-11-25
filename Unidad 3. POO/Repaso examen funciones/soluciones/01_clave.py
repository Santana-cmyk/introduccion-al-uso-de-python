def validar_clave(clave):
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digitos = "0123456789"
    if not 6 <= len(clave) <= 12 or clave[0] not in letras:
        return False

    tiene_digito = False
    for caracter in clave:
        if caracter in digitos:
            tiene_digito = True
        elif caracter not in letras and caracter != "-":
            return False

    return tiene_digito


if __name__ == "__main__":
    assert validar_clave("Aula-3") is True
    assert validar_clave("Aula-ab") is False
    assert validar_clave("3Aula-") is False
    assert validar_clave("Aula_3") is False
    assert validar_clave("") is False
