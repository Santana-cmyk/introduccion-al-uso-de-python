# marcadores

Recibe una lista de marcadores con dos enteros no negativos por partido (goles a favor y en contra). Devuelve un diccionario con victorias, empates, derrotas, puntos y diferencia de goles. Una victoria suma 3 puntos y un empate suma 1. La diferencia es goles a favor menos goles en contra.

Firma propuesta

```python
def resumir_marcadores(marcadores)
```

Casos de comprobación

```python
assert resumir_marcadores([(2, 0), (1, 1), (0, 3)]) == {"victorias": 1, "empates": 1, "derrotas": 1, "puntos": 4, "diferencia": -1}
assert resumir_marcadores([]) == {"victorias": 0, "empates": 0, "derrotas": 0, "puntos": 0, "diferencia": 0}
```
