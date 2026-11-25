# inventario

Recibe un diccionario con las existencias por producto y una lista de pares (producto, cantidad solicitada). Procesa los pedidos en orden. Acepta un pedido si la cantidad es positiva, el producto existe y queda stock suficiente. Descuenta las unidades solo de los pedidos aceptados. Devuelve el inventario final y la lista de pedidos rechazados en el orden en que llegaron. Conserva el inventario original.

Firma propuesta

```python
def preparar_pedidos(inventario, pedidos)
```

Casos de comprobación

```python
assert preparar_pedidos({"pocion": 3}, [("pocion", 2), ("pocion", 2), ("pocion", 1), ("llave", 1), ("pocion", 0)]) == ({"pocion": 0}, [("pocion", 2), ("llave", 1), ("pocion", 0)])
assert preparar_pedidos({"pocion": 3}, []) == ({"pocion": 3}, [])
```
