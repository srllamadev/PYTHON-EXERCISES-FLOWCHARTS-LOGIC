# Ejercicio Básico de Tuplas en Python

## ¿Qué son las tuplas?
Las **tuplas** son estructuras de datos en Python con estas características:
- **Inmutables**: No se pueden modificar después de su creación
- **Ordenadas**: Mantienen el orden de inserción
- **Indexables**: Se accede a elementos por posición (índices)
- **Heterogéneas**: Pueden almacenar diferentes tipos de datos
- Sintaxis: Se crean con paréntesis `()` o solo comas

### Casos de uso comunes:
1. Almacenar datos inmutables (coordenadas, configuraciones)
2. Retornar múltiples valores desde una función
3. Claves en diccionarios (cuando se necesitan valores compuestos)
4. Proteger datos contra modificaciones accidentales
5. Mejor rendimiento que listas para operaciones de solo lectura

---

## Ejercicio Práctico

```python
# 1. Creación de tupla
colores = ('rojo', 'verde', 'azul')
print(f"Tupla original: {colores}")

# 2. Acceso por índice
print(f"Segundo elemento: {colores[1]}")  # verde

# 3. Intento de modificación (ERROR)
# colores[0] = 'amarillo'  # TypeError: 'tuple' object does not support item assignment

# 4. Conversión a lista para modificación
lista_colores = list(colores)
lista_colores.append('amarillo')
nueva_tupla = tuple(lista_colores)
print(f"Tupla modificada: {nueva_tupla}")  # ('rojo', 'verde', 'azul', 'amarillo')

# 5. Conteo de elementos
print(f"Veces 'azul': {colores.count('azul')}")  # 1

# 6. Búsqueda de posición
print(f"Posición de 'verde': {colores.index('verde')}")  # 1

# 7. Tupla unitaria (¡atención a la coma!)
tupla_unitario = ('solo',)
print(f"Tipo: {type(tupla_unitario)}")  # <class 'tuple'>

# 8. Desempaquetado
r, v, a = colores
print(f"Rojo: {r}, Verde: {v}, Azul: {a}")
