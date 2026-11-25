# racha

Recibe una lista de puntuaciones enteras y un mínimo (10 por defecto). Busca el tramo consecutivo más largo con puntuaciones mayores o iguales al mínimo. Devuelve el índice inicial y la longitud. Si hay empate, conserva el primer tramo. Si no hay ninguno, devuelve (-1, 0).

Firma propuesta

```python
def buscar_racha(puntuaciones, minimo=10)
```

Casos de comprobación

```python
assert buscar_racha([9, 11, 10, 2, 10, 12]) == (1, 2)
assert buscar_racha([12, 2, 11, 12, 13]) == (2, 3)
assert buscar_racha([1, 5, 5], 5) == (1, 2)
assert buscar_racha([9]) == (-1, 0)
assert buscar_racha([]) == (-1, 0)
```
