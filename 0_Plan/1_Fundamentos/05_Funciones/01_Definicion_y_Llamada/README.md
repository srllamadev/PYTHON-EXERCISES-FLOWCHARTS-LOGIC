# Definición y Llamada de Funciones

## Objetivos de Aprendizaje
- Entender qué es una función y para qué sirve
- Aprender la sintaxis para definir funciones con `def`
- Saber cómo llamar (invocar) una función
- Reconocer la diferencia entre definir y llamar

## Conceptos Teóricos

### ¿Qué es una Función?
Una función es un bloque de código **nombrado y reutilizable** que realiza una tarea específica. En lugar de repetir código, lo agrupamos dentro de una función y la llamamos cuando la necesitamos.

### Sintaxis Básica

```python
def nombre_de_la_funcion():
    # cuerpo de la función
    instruccion_1
    instruccion_2
```

- `def` → palabra clave que indica que estamos definiendo una función
- `nombre_de_la_funcion` → nombre en snake_case
- `:` → indica el inicio del bloque
- El cuerpo debe estar **indentado** (4 espacios)

### Llamar a una Función

```python
nombre_de_la_funcion()
```

Solo se ejecuta el código cuando la llamamos. Definir no ejecuta.

### Ejemplo Completo

```python
def saludar():
    print("¡Hola, mundo!")

saludar()   # Output: ¡Hola, mundo!
saludar()   # Se puede llamar múltiples veces
```

### Ventajas de las Funciones

| Sin Funciones | Con Funciones |
|---|---|
| Código repetido | Código reutilizable |
| Difícil de mantener | Fácil de mantener |
| Sin organización | Código organizado |
| Difícil de probar | Fácil de probar |

### Buenas Prácticas al Nombrar Funciones

✅ Usa verbos descriptivos: `calcular_area()`, `mostrar_menu()`  
✅ Usa snake_case: `mi_funcion()`  
✅ Nombres cortos pero claros  
❌ Evita nombres genéricos: `funcion1()`, `hacer()`  

## Recursos Adicionales
- [Python Docs - Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
