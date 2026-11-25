# clave

Valida una clave de 6 a 12 caracteres. Solo admite letras ASCII, dígitos y guiones. Debe empezar por una letra y contener al menos un dígito. Devuelve un booleano.

Firma propuesta

```python
def validar_clave(clave)
```

Casos de comprobación

```python
assert validar_clave("Aula-3") is True
assert validar_clave("Aula-ab") is False
assert validar_clave("3Aula-") is False
assert validar_clave("Aula_3") is False
assert validar_clave("") is False
```
