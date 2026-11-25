"""
inventario

Recibe un diccionario con las existencias por producto y una lista de pares
(producto, cantidad solicitada). Procesa los pedidos en orden. Acepta un
pedido si la cantidad es positiva, el producto existe y queda stock
suficiente. Descuenta las unidades solo de los pedidos aceptados. Devuelve
el inventario final y la lista de pedidos rechazados en el orden en que
llegaron. Conserva el inventario original.
"""

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
