# While Loops

## Concepto
El bucle `while` ejecuta un bloque de código mientras una condición sea verdadera.

## Sintaxis Básica
```python
while condicion:
    # código a ejecutar
    # actualizar condición
```

## Características
- Se evalúa la condición ANTES de cada iteración
- Si la condición es False desde el inicio, el código nunca se ejecuta
- Es crucial modificar la condición dentro del bucle para evitar bucles infinitos

## Casos de Uso
- Cuando no se conoce de antemano cuántas iteraciones se necesitan
- Validación de entrada de usuario
- Procesos que dependen de condiciones dinámicas
- Juegos y simulaciones

## Puntos Importantes
⚠️ **Evitar bucles infinitos**: Asegúrate de que la condición eventualmente sea False
✅ **Condición clara**: La condición debe ser fácil de entender y verificar
