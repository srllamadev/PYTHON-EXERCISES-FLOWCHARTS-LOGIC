# Listas en Python

## Características de las Listas

- **Mutabilidad**: Las listas pueden modificarse después de su creación.
- **Indexación**: Acceso a elementos mediante índices (comienza en 0).
- **Slicing**: Se puede usar `lista[inicio:fin:paso]` para obtener sub-listas.

## Métodos Esenciales

- **`.append()`**: Añade un elemento al final de la lista.
- **`.insert()`**: Inserta un elemento en una posición específica.
- **`.pop()`**: Elimina un elemento por índice y devuelve su valor.
- **`.remove()`**: Elimina un elemento por valor.
- **`.sort()`**: Ordena la lista in-place.

## Comprensión de Listas

Forma concisa de crear listas. Por ejemplo:

```python
cuadrados = [x**2 for x in range(10)]