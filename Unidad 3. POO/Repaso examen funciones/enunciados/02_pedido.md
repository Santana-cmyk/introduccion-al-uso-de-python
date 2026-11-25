# pedido

Calcula el precio de un pedido. Recibe una lista de precios enteros no negativos en céntimos y un cupón. Ignora espacios externos y diferencias de mayúsculas en el cupón. A partir de 3000 céntimos, AHORRO10 descuenta un 10 % (redondeado hacia abajo a céntimos) y el envío es gratis con cualquier cupón. Por debajo de 3000, el envío cuesta 350. Devuelve subtotal, descuento y total en ese orden. Un pedido vacío devuelve (0, 0, 0).

Firma propuesta

```python
def calcular_pedido(precios, cupon="")
```

Casos de comprobación

```python
assert calcular_pedido([1500, 1509], " ahorro10 ") == (3009, 300, 2709)
assert calcular_pedido([2999], "AHORRO10") == (2999, 0, 3349)
assert calcular_pedido([3000]) == (3000, 0, 3000)
assert calcular_pedido([]) == (0, 0, 0)
```
