"""
EJERCICIO 9: Contar cuántos dígitos son pares e impares

ANÁLISIS DEL PROBLEMA:
====================
Entrada: 
  - N: número entero positivo

Proceso:
  - Extraer cada dígito del número usando módulo 10
  - Verificar si el dígito es par o impar
  - Incrementar el contador correspondiente
  - Eliminar el dígito procesado con división entera

Salida:
  - cantidad_pares: número de dígitos pares
  - cantidad_impares: número de dígitos impares

GUÍA PARA DIAGRAMA DE FLUJO:
============================
1. INICIO (óvalo)
2. "Ingresar N" (paralelogramo - entrada)
3. "cantidad_pares = 0" (rectángulo)
4. "cantidad_impares = 0" (rectángulo)
5. "¿N > 0?" (rombo - decisión)
   - SI: continuar
   - NO: ir a paso 10
6. "digito = N % 10" (rectángulo - extraer último dígito)
7. "¿digito % 2 == 0?" (rombo - ¿es par?)
   - SI: "cantidad_pares = cantidad_pares + 1" (rectángulo)
   - NO: "cantidad_impares = cantidad_impares + 1" (rectángulo)
8. "N = N // 10" (rectángulo - eliminar último dígito)
9. Volver a paso 5
10. "Imprimir 'Pares:', cantidad_pares" (paralelogramo)
11. "Imprimir 'Impares:', cantidad_impares" (paralelogramo)
12. FIN (óvalo)

LÓGICA MATEMÁTICA:
- N % 10: obtiene el último dígito
- N // 10: elimina el último dígito
- digito % 2 == 0: verifica si es par
- Dígitos pares: 0, 2, 4, 6, 8
- Dígitos impares: 1, 3, 5, 7, 9

PRUEBA DE ESCRITORIO:
====================
Variables clave para Excel:
- N: número (se modifica)
- digito: dígito actual extraído
- es_par: TRUE/FALSE
- cantidad_pares: contador de pares
- cantidad_impares: contador de impares

Ejemplo N=24681:
| N     | digito | es_par | cantidad_pares | cantidad_impares |
|-------|--------|--------|----------------|------------------|
| 24681 | 1      | FALSE  | 0              | 1                |
| 2468  | 8      | TRUE   | 1              | 1                |
| 246   | 6      | TRUE   | 2              | 1                |
| 24    | 4      | TRUE   | 3              | 1                |
| 2     | 2      | TRUE   | 4              | 1                |
| 0     | -      | -      | 4              | 1                |
| Resultado: Pares=4, Impares=1                               |

Ejemplo N=13579:
| N     | digito | es_par | cantidad_pares | cantidad_impares |
|-------|--------|--------|----------------|------------------|
| 13579 | 9      | FALSE  | 0              | 1                |
| 1357  | 7      | FALSE  | 0              | 2                |
| 135   | 5      | FALSE  | 0              | 3                |
| 13    | 3      | FALSE  | 0              | 4                |
| 1     | 1      | FALSE  | 0              | 5                |
| 0     | -      | -      | 0              | 5                |
| Resultado: Pares=0, Impares=5                               |

Ejemplo N=2048:
| N    | digito | es_par | cantidad_pares | cantidad_impares |
|------|--------|--------|----------------|------------------|
| 2048 | 8      | TRUE   | 1              | 0                |
| 204  | 4      | TRUE   | 2              | 0                |
| 20   | 0      | TRUE   | 3              | 0                |
| 2    | 2      | TRUE   | 4              | 0                |
| 0    | -      | -      | 4              | 0                |
| Resultado: Pares=4, Impares=0                               |

Ejemplo N=102345:
| N      | digito | es_par | cantidad_pares | cantidad_impares |
|--------|--------|--------|----------------|------------------|
| 102345 | 5      | FALSE  | 0              | 1                |
| 10234  | 4      | TRUE   | 1              | 1                |
| 1023   | 3      | FALSE  | 1              | 2                |
| 102    | 2      | TRUE   | 2              | 2                |
| 10     | 0      | TRUE   | 3              | 2                |
| 1      | 1      | FALSE  | 3              | 3                |
| 0      | -      | -      | 3              | 3                |
| Resultado: Pares=3, Impares=3                               |
"""

# Ingreso de dato
N = int(input("Ingrese un número: "))

# Inicialización
cantidad_pares = 0
cantidad_impares = 0

# Clasificar dígitos
while N > 0:
    digito = N % 10  # Extraer último dígito
    
    if digito % 2 == 0:  # Si es par
        cantidad_pares = cantidad_pares + 1
    else:  # Si es impar
        cantidad_impares = cantidad_impares + 1
    
    N = N // 10  # Eliminar último dígito

# Salida
print("Dígitos pares:", cantidad_pares)
print("Dígitos impares:", cantidad_impares)
