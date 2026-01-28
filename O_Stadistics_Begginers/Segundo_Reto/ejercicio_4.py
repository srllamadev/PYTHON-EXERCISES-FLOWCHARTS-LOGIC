"""
EJERCICIO 4: Invertir un número entero N

ANÁLISIS DEL PROBLEMA:
====================
Entrada: 
  - N: número entero positivo

Proceso:
  - Extraer cada dígito del número de derecha a izquierda
  - Reconstruir el número en orden inverso
  - Usar operaciones matemáticas: % (módulo) y // (división entera)

Salida:
  - numero_invertido: número con dígitos en orden inverso

GUÍA PARA DIAGRAMA DE FLUJO:
============================
1. INICIO (óvalo)
2. "Ingresar N" (paralelogramo - entrada)
3. "numero_invertido = 0" (rectángulo)
4. "¿N > 0?" (rombo - decisión)
   - SI: continuar
   - NO: ir a paso 8
5. "digito = N % 10" (rectángulo - extraer último dígito)
6. "numero_invertido = numero_invertido * 10 + digito" (rectángulo)
7. "N = N // 10" (rectángulo - eliminar último dígito), volver a paso 4
8. "Imprimir numero_invertido" (paralelogramo - salida)
9. FIN (óvalo)

LÓGICA MATEMÁTICA:
- N % 10: obtiene el último dígito
- N // 10: elimina el último dígito
- numero_invertido * 10 + digito: agrega el dígito al final del invertido

Ejemplo: 123 → 321
- 123 % 10 = 3 → invertido = 0*10 + 3 = 3
- 12 % 10 = 2 → invertido = 3*10 + 2 = 32
- 1 % 10 = 1 → invertido = 32*10 + 1 = 321

PRUEBA DE ESCRITORIO:
====================
Variables clave para Excel:
- N: número original (se modifica)
- digito: dígito actual extraído
- numero_invertido: número resultante
- operacion: cálculo realizado

Ejemplo N=12345:
| N     | digito | numero_invertido | operacion        |
|-------|--------|------------------|------------------|
| 12345 | 5      | 5                | 0*10 + 5 = 5     |
| 1234  | 4      | 54               | 5*10 + 4 = 54    |
| 123   | 3      | 543              | 54*10 + 3 = 543  |
| 12    | 2      | 5432             | 543*10 + 2 = 5432|
| 1     | 1      | 54321            | 5432*10 + 1 = 54321|
| 0     | -      | 54321            | -                |

Ejemplo N=7890:
| N    | digito | numero_invertido | operacion       |
|------|--------|------------------|-----------------|
| 7890 | 0      | 0                | 0*10 + 0 = 0    |
| 789  | 9      | 9                | 0*10 + 9 = 9    |
| 78   | 8      | 98               | 9*10 + 8 = 98   |
| 7    | 7      | 987              | 98*10 + 7 = 987 |
| 0    | -      | 987              | -               |

Ejemplo N=100:
| N   | digito | numero_invertido | operacion     |
|-----|--------|------------------|---------------|
| 100 | 0      | 0                | 0*10 + 0 = 0  |
| 10  | 0      | 0                | 0*10 + 0 = 0  |
| 1   | 1      | 1                | 0*10 + 1 = 1  |
| 0   | -      | 1                | -             |
"""

# Ingreso de dato
N = int(input("Ingrese un número: "))

# Inicialización
numero_invertido = 0

# Invertir el número
while N > 0:
    digito = N % 10  # Extraer último dígito
    numero_invertido = numero_invertido * 10 + digito  # Agregar al invertido
    N = N // 10  # Eliminar último dígito

# Salida
print("Número invertido:", numero_invertido)
