"""
EJERCICIO 7: Contar la cantidad de dígitos de un número

ANÁLISIS DEL PROBLEMA:
====================
Entrada: 
  - N: número entero positivo

Proceso:
  - Eliminar dígitos uno por uno usando división entera
  - Contar cuántas veces se puede dividir hasta llegar a 0
  - Cada división por 10 elimina un dígito

Salida:
  - cantidad_digitos: número de dígitos que tiene N

GUÍA PARA DIAGRAMA DE FLUJO:
============================
1. INICIO (óvalo)
2. "Ingresar N" (paralelogramo - entrada)
3. "cantidad_digitos = 0" (rectángulo)
4. "¿N > 0?" (rombo - decisión)
   - SI: continuar
   - NO: ir a paso 7
5. "cantidad_digitos = cantidad_digitos + 1" (rectángulo)
6. "N = N // 10" (rectángulo - eliminar último dígito), volver a paso 4
7. "Imprimir cantidad_digitos" (paralelogramo - salida)
8. FIN (óvalo)

LÓGICA MATEMÁTICA:
- N // 10: elimina el último dígito
- Cada iteración cuenta un dígito
- Ejemplos:
  * 12345 → 5 dígitos
  * 789 → 3 dígitos
  * 42 → 2 dígitos
  * 5 → 1 dígito

PRUEBA DE ESCRITORIO:
====================
Variables clave para Excel:
- N: número (se modifica)
- cantidad_digitos: contador de dígitos
- iteracion: número de iteración

Ejemplo N=12345:
| iteracion | N     | cantidad_digitos | N > 0 | operacion      |
|-----------|-------|------------------|-------|----------------|
| 0         | 12345 | 0                | TRUE  | -              |
| 1         | 1234  | 1                | TRUE  | 12345 // 10    |
| 2         | 123   | 2                | TRUE  | 1234 // 10     |
| 3         | 12    | 3                | TRUE  | 123 // 10      |
| 4         | 1     | 4                | TRUE  | 12 // 10       |
| 5         | 0     | 5                | FALSE | 1 // 10        |
| Resultado: 5 dígitos                                         |

Ejemplo N=789:
| iteracion | N   | cantidad_digitos | N > 0 | operacion   |
|-----------|-----|------------------|-------|-------------|
| 0         | 789 | 0                | TRUE  | -           |
| 1         | 78  | 1                | TRUE  | 789 // 10   |
| 2         | 7   | 2                | TRUE  | 78 // 10    |
| 3         | 0   | 3                | FALSE | 7 // 10     |
| Resultado: 3 dígitos                                    |

Ejemplo N=7:
| iteracion | N | cantidad_digitos | N > 0 | operacion |
|-----------|---|------------------|-------|-----------|
| 0         | 7 | 0                | TRUE  | -         |
| 1         | 0 | 1                | FALSE | 7 // 10   |
| Resultado: 1 dígito                                   |

Ejemplo N=1000:
| iteracion | N    | cantidad_digitos | N > 0 | operacion  |
|-----------|------|------------------|-------|------------|
| 0         | 1000 | 0                | TRUE  | -          |
| 1         | 100  | 1                | TRUE  | 1000 // 10 |
| 2         | 10   | 2                | TRUE  | 100 // 10  |
| 3         | 1    | 3                | TRUE  | 10 // 10   |
| 4         | 0    | 4                | FALSE | 1 // 10    |
| Resultado: 4 dígitos                                   |
"""

# Ingreso de dato
N = int(input("Ingrese un número: "))

# Inicialización
cantidad_digitos = 0

# Contar dígitos
while N > 0:
    cantidad_digitos = cantidad_digitos + 1
    N = N // 10  # Eliminar último dígito

# Salida
print("Cantidad de dígitos:", cantidad_digitos)
