"""
EJERCICIO 3: Eliminar los dígitos pares de un número N

ANÁLISIS DEL PROBLEMA:
====================
Entrada: 
  - N: número entero positivo

Proceso:
  - Extraer cada dígito del número de derecha a izquierda
  - Si el dígito es impar, incorporarlo al nuevo número
  - Reconstruir el número solo con dígitos impares
  - Usar posición para mantener el orden correcto

Salida:
  - numero_sin_pares: número resultante sin dígitos pares

GUÍA PARA DIAGRAMA DE FLUJO:
============================
1. INICIO (óvalo)
2. "Ingresar N" (paralelogramo - entrada)
3. "numero_sin_pares = 0" (rectángulo)
4. "posicion = 1" (rectángulo)
5. "¿N > 0?" (rombo - decisión)
   - SI: continuar
   - NO: ir a paso 11
6. "digito = N % 10" (rectángulo - extraer último dígito)
7. "¿digito % 2 != 0?" (rombo - ¿es impar?)
   - SI: continuar
   - NO: ir a paso 9
8. "numero_sin_pares = numero_sin_pares + digito * posicion" (rectángulo)
   "posicion = posicion * 10" (rectángulo)
9. "N = N // 10" (rectángulo - eliminar último dígito)
10. Volver a paso 5
11. "Imprimir numero_sin_pares" (paralelogramo - salida)
12. FIN (óvalo)

LÓGICA MATEMÁTICA:
- N % 10: obtiene el último dígito
- N // 10: elimina el último dígito
- digito % 2 != 0: verifica si es impar
- Reconstruir: digito * posicion (1, 10, 100, ...)

PRUEBA DE ESCRITORIO:
====================
Variables clave para Excel:
- N: número original (se modifica)
- digito: dígito actual extraído
- es_impar: TRUE/FALSE
- numero_sin_pares: número resultante
- posicion: multiplicador (1, 10, 100, ...)

Ejemplo N=24681:
| N     | digito | es_impar | numero_sin_pares | posicion |
|-------|--------|----------|------------------|----------|
| 24681 | 1      | TRUE     | 1                | 1        |
| 2468  | 8      | FALSE    | 1                | 10       |
| 246   | 6      | FALSE    | 1                | 10       |
| 24    | 4      | FALSE    | 1                | 10       |
| 2     | 2      | FALSE    | 1                | 10       |
| 0     | -      | -        | 1                | -        |

Ejemplo N=13579:
| N     | digito | es_impar | numero_sin_pares | posicion |
|-------|--------|----------|------------------|----------|
| 13579 | 9      | TRUE     | 9                | 1        |
| 1357  | 7      | TRUE     | 79               | 10       |
| 135   | 5      | TRUE     | 579              | 100      |
| 13    | 3      | TRUE     | 3579             | 1000     |
| 1     | 1      | TRUE     | 13579            | 10000    |
| 0     | -      | -        | 13579            | -        |

Ejemplo N=2468:
| N    | digito | es_impar | numero_sin_pares | posicion |
|------|--------|----------|------------------|----------|
| 2468 | 8      | FALSE    | 0                | 1        |
| 246  | 6      | FALSE    | 0                | 1        |
| 24   | 4      | FALSE    | 0                | 1        |
| 2    | 2      | FALSE    | 0                | 1        |
| 0    | -      | -        | 0                | -        |
"""

# Ingreso de dato
N = int(input("Ingrese un número: "))

# Inicialización
numero_sin_pares = 0
posicion = 1

# Procesar cada dígito
while N > 0:
    digito = N % 10  # Extraer último dígito
    
    # Si el dígito es impar, agregarlo al nuevo número
    if digito % 2 != 0:
        numero_sin_pares = numero_sin_pares + digito * posicion
        posicion = posicion * 10
    
    N = N // 10  # Eliminar último dígito

# Salida
print("Número sin dígitos pares:", numero_sin_pares)
