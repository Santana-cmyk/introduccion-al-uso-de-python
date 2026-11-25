def preparar_pedidos(inventario, pedidos):
    disponibles = inventario.copy()
    rechazados = []
    for producto, cantidad in pedidos:
        if cantidad > 0 and producto in disponibles and disponibles[producto] >= cantidad:
            disponibles[producto] -= cantidad
        else:
            rechazados.append((producto, cantidad))
    return disponibles, rechazados


if __name__ == "__main__":
    assert preparar_pedidos({"pocion": 3}, [("pocion", 2), ("pocion", 2), ("pocion", 1), ("llave", 1), ("pocion", 0)]) == ({"pocion": 0}, [("pocion", 2), ("llave", 1), ("pocion", 0)])
    assert preparar_pedidos({"pocion": 3}, []) == ({"pocion": 3}, [])
    original = {"pocion": 1}
    preparar_pedidos(original, [("pocion", 1)])
    assert original == {"pocion": 1}
