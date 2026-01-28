# Segundo Reto - INF-111
## Algoritmos y Programación en Python

### 📚 Descripción
Colección de 10 ejercicios de algoritmia que abarcan:
- **Parte 1:** Verificación de números primos, MCD mediante Euclides
- **Parte 2:** Manipulación de dígitos usando operaciones matemáticas

---

## 📋 Lista de Ejercicios

### Ejercicio 1: Números Primos hasta N
**Archivo:** `ejercicio_1.py`

**Descripción:** Imprime todos los números primos desde 2 hasta N y calcula su suma.

**Entrada:** 
- N: número entero positivo

**Salida:**
- Lista de números primos
- Suma total de los primos

**Ejemplo:**
```
Entrada: 10
Salida: 
Primos: 2, 3, 5, 7
Suma: 17
```

**Concepto:** Un número primo tiene exactamente 2 divisores (1 y él mismo).

---

### Ejercicio 2: Máximo Común Divisor (MCD)
**Archivo:** `ejercicio_2.py`

**Descripción:** Calcula el MCD de dos números usando el Algoritmo de Euclides.

**Entrada:**
- a: primer número entero
- b: segundo número entero

**Salida:**
- MCD de a y b

**Ejemplo:**
```
Entrada: 48, 18
Salida: MCD: 6
```

**Algoritmo de Euclides:**
```
MCD(a, b) = MCD(b, a % b)
Repite hasta que b = 0
```

---

### Ejercicio 3: Eliminar Dígitos Pares
**Archivo:** `ejercicio_3.py`

**Descripción:** Elimina todos los dígitos pares de un número, conservando solo los impares.

**Entrada:**
- N: número entero positivo

**Salida:**
- Número sin dígitos pares

**Ejemplo:**
```
Entrada: 24681
Salida: Número sin dígitos pares: 1

Entrada: 13579
Salida: Número sin dígitos pares: 13579
```

**Nota:** Usa operaciones matemáticas (%, //, *), no strings.

---

### Ejercicio 4: Invertir Número
**Archivo:** `ejercicio_4.py`

**Descripción:** Invierte el orden de los dígitos de un número.

**Entrada:**
- N: número entero positivo

**Salida:**
- Número invertido

**Ejemplo:**
```
Entrada: 12345
Salida: Número invertido: 54321

Entrada: 7890
Salida: Número invertido: 987
```

**Lógica:**
- Extraer dígitos de derecha a izquierda
- Reconstruir en orden inverso

---

### Ejercicio 5: Verificar Palíndromo
**Archivo:** `ejercicio_5.py`

**Descripción:** Verifica si un número es palíndromo (se lee igual al derecho y al revés).

**Entrada:**
- N: número entero positivo

**Salida:**
- "Es palíndromo" o "No es palíndromo"

**Ejemplo:**
```
Entrada: 12321
Salida: Es palíndromo

Entrada: 12345
Salida: No es palíndromo
```

**Ejemplos de palíndromos:** 121, 1331, 12321, 9009

---

### Ejercicio 6: Producto por Sumas Sucesivas
**Archivo:** `ejercicio_6.py`

**Descripción:** Multiplica dos números mediante sumas sucesivas (sin usar operador *).

**Entrada:**
- a: primer número
- b: segundo número

**Salida:**
- Producto de a × b

**Ejemplo:**
```
Entrada: 6, 4
Salida: Producto: 24
(6 + 6 + 6 + 6 = 24)
```

**Concepto:** a × b = a + a + a + ... (b veces)

---

### Ejercicio 7: Contar Dígitos
**Archivo:** `ejercicio_7.py`

**Descripción:** Cuenta cuántos dígitos tiene un número.

**Entrada:**
- N: número entero positivo

**Salida:**
- Cantidad de dígitos

**Ejemplo:**
```
Entrada: 12345
Salida: Cantidad de dígitos: 5

Entrada: 789
Salida: Cantidad de dígitos: 3
```

**Lógica:** Dividir por 10 hasta llegar a 0, contar iteraciones.

---

### Ejercicio 8: Sumar Dígitos Pares
**Archivo:** `ejercicio_8.py`

**Descripción:** Suma solo los dígitos pares de un número.

**Entrada:**
- N: número entero positivo

**Salida:**
- Suma de dígitos pares

**Ejemplo:**
```
Entrada: 24681
Salida: Suma de dígitos pares: 20
(2 + 4 + 6 + 8 = 20)

Entrada: 13579
Salida: Suma de dígitos pares: 0
```

**Dígitos pares:** 0, 2, 4, 6, 8

---

### Ejercicio 9: Contar Pares e Impares
**Archivo:** `ejercicio_9.py`

**Descripción:** Cuenta cuántos dígitos pares e impares tiene un número.

**Entrada:**
- N: número entero positivo

**Salida:**
- Cantidad de dígitos pares
- Cantidad de dígitos impares

**Ejemplo:**
```
Entrada: 24681
Salida: 
Dígitos pares: 4
Dígitos impares: 1

Entrada: 102345
Salida:
Dígitos pares: 3
Dígitos impares: 3
```

---

### Ejercicio 10: Sumar Todos los Dígitos
**Archivo:** `ejercicio_10.py`

**Descripción:** Suma todos los dígitos de un número.

**Entrada:**
- N: número entero positivo

**Salida:**
- Suma total de dígitos

**Ejemplo:**
```
Entrada: 23
Salida: Suma de los dígitos: 5
(2 + 3 = 5)

Entrada: 456
Salida: Suma de los dígitos: 15
(4 + 5 + 6 = 15)
```

---

## 🔧 Operaciones Matemáticas Clave

Todos los ejercicios usan **operaciones matemáticas** en lugar de funciones de strings:

| Operación | Descripción | Ejemplo |
|-----------|-------------|---------|
| `N % 10` | Obtiene el último dígito | `123 % 10 = 3` |
| `N // 10` | Elimina el último dígito | `123 // 10 = 12` |
| `digito % 2 == 0` | Verifica si es par | `4 % 2 == 0` → TRUE |
| `num * 10 + digito` | Agrega dígito al final | `12 * 10 + 3 = 123` |

---

## 📊 Estructura de Cada Ejercicio

Cada archivo `.py` incluye:

1. **Análisis del Problema**
   - Entrada
   - Proceso
   - Salida

2. **Guía para Diagrama de Flujo**
   - Paso a paso con formas específicas (óvalos, rectángulos, rombos)
   - Ideal para trasladar a draw.io

3. **Prueba de Escritorio**
   - Tablas con variables clave
   - Ejemplos completos de ejecución
   - Listas para usar en Excel

4. **Código Python Funcional**
   - Variables con nombres descriptivos
   - Comentarios explicativos
   - Implementación clara del algoritmo

---

## 🚀 Cómo Usar

### Ejecutar un ejercicio:
```bash
python ejercicio_1.py
```

### Pruebas de Escritorio:
1. Abre Excel
2. Crea columnas para cada variable del ejercicio
3. Sigue la tabla de ejemplo en los comentarios del código
4. Verifica que tu lógica coincida con la ejecución

### Diagramas de Flujo:
1. Abre draw.io
2. Sigue la guía paso a paso en cada ejercicio
3. Usa las formas correctas:
   - **Óvalo:** INICIO/FIN
   - **Paralelogramo:** Entrada/Salida
   - **Rectángulo:** Proceso/Asignación
   - **Rombo:** Decisión/Condición

---

## 📝 Notas Importantes

- ✅ **Usa operaciones matemáticas** para manipular dígitos
- ❌ **NO uses funciones de strings** (str, reverse, etc.)
- ✅ **Variables descriptivas** (suma_pares, cantidad_digitos, etc.)
- ✅ **Comentarios claros** en cada paso del algoritmo

---

## 🎯 Objetivos de Aprendizaje

1. Manipulación de números con operadores matemáticos
2. Estructuras de control (while, if-else)
3. Algoritmos clásicos (Euclides, verificación de primos)
4. Diseño de algoritmos con diagramas de flujo
5. Validación mediante pruebas de escritorio

---

## 👨‍💻 Autor
Ejercicios para la materia **Introducción a la Informática (INF-111)**

---

## 📚 Referencias

- Algoritmo de Euclides
- Números primos
- Manipulación de dígitos
- Palíndromos
- Operaciones matemáticas básicas en Python

---

**¡Éxito en tus estudios! 🚀**
