# Break, Continue, Pass

## Conceptos
Estas tres palabras clave permiten controlar el flujo de ejecución dentro de bucles.

## Break
**Función**: Termina el bucle inmediatamente y sale de él.

```python
for i in range(10):
    if i == 5:
        break  # Sale del bucle cuando i es 5
    print(i)  # Imprime: 0, 1, 2, 3, 4
```

**Casos de uso**:
- Búsqueda: salir cuando encuentras lo que buscas
- Validación: salir cuando se cumple una condición
- Límites: detener cuando se alcanza un límite

## Continue
**Función**: Salta el resto del código en la iteración actual y pasa a la siguiente.

```python
for i in range(5):
    if i == 2:
        continue  # Salta cuando i es 2
    print(i)  # Imprime: 0, 1, 3, 4 (omite el 2)
```

**Casos de uso**:
- Filtrado: omitir elementos que no cumplen condiciones
- Validación: saltar datos inválidos
- Procesamiento selectivo

## Pass
**Función**: No hace nada, es un placeholder.

```python
for i in range(5):
    if i == 2:
        pass  # No hace nada, solo continúa
    print(i)  # Imprime: 0, 1, 2, 3, 4
```

**Casos de uso**:
- Código incompleto: marcar secciones por implementar
- Estructuras vacías: clases o funciones que se llenarán después
- Sintaxis requerida: cuando Python requiere código pero no quieres hacer nada

## Diferencias Clave

| Palabra | Acción | Efecto en el bucle | Continúa después |
|---------|--------|-------------------|------------------|
| `break` | Sale completamente | Termina | No (sale) |
| `continue` | Salta iteración actual | Continúa a siguiente | Sí |
| `pass` | No hace nada | Continúa normal | Sí |

## Else en Bucles
Python permite `else` después de bucles, se ejecuta si el bucle termina normalmente (sin `break`).

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Bucle completado sin break")
```
