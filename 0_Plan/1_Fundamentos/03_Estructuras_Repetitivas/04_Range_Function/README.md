# Range Function

## Concepto
`range()` es una función incorporada que genera una secuencia de números, muy útil para controlar bucles.

## Sintaxis

### 1. range(stop)
Genera números desde 0 hasta stop-1
```python
range(5)  # 0, 1, 2, 3, 4
```

### 2. range(start, stop)
Genera números desde start hasta stop-1
```python
range(2, 7)  # 2, 3, 4, 5, 6
```

### 3. range(start, stop, step)
Genera números desde start hasta stop-1, incrementando en step
```python
range(0, 10, 2)  # 0, 2, 4, 6, 8
range(10, 0, -1)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

## Características Importantes

### Es un objeto iterable, NO una lista
```python
>>> range(5)
range(0, 5)  # No es [0, 1, 2, 3, 4]

>>> list(range(5))
[0, 1, 2, 3, 4]  # Convertir a lista
```

### Es eficiente en memoria
- No almacena todos los valores en memoria
- Genera valores "sobre la marcha" (lazy evaluation)
- Ideal para bucles grandes

### El stop es exclusivo
```python
range(1, 5)  # 1, 2, 3, 4 (el 5 NO se incluye)
```

## Patrones Comunes

### Repetir N veces
```python
for _ in range(5):
    print("Hola")
```

### Generar índices
```python
lista = ['a', 'b', 'c']
for i in range(len(lista)):
    print(f"{i}: {lista[i]}")
```

### Números descendentes
```python
for i in range(10, 0, -1):
    print(i)  # Cuenta regresiva
```

### Pasos personalizados
```python
for i in range(0, 100, 10):
    print(i)  # 0, 10, 20, 30, ..., 90
```

## Casos de Uso
1. **Iteraciones controladas**: Cuando necesitas un número exacto de repeticiones
2. **Generar secuencias**: Crear listas, tuplas de números
3. **Índices**: Acceso a elementos por posición
4. **Matemáticas**: Series numéricas, progresiones
5. **Cronómetros**: Cuentas regresivas, temporizadores

## Ventajas vs otras alternativas
✅ Más eficiente que crear listas manualmente  
✅ Sintaxis clara y concisa  
✅ Soporta pasos negativos (reversa)  
✅ Ideal para bucles for
