"""
EJERCICIO 8: Sumar los dígitos pares de un número

ANÁLISIS DEL PROBLEMA:
====================
Entrada: 
  - N: número entero positivo

Proceso:
  - Extraer cada dígito del número usando módulo 10
  - Verificar si el dígito es par (divisible por 2)
  - Si es par, sumarlo al acumulador
  - Eliminar el dígito procesado con división entera

Salida:
  - suma_pares: suma de todos los dígitos pares

GUÍA PARA DIAGRAMA DE FLUJO:
============================
1. INICIO (óvalo)
2. "Ingresar N" (paralelogramo - entrada)
3. "suma_pares = 0" (rectángulo)
4. "¿N > 0?" (rombo - decisión)
   - SI: continuar
   - NO: ir a paso 9
5. "digito = N % 10" (rectángulo - extraer último dígito)
6. "¿digito % 2 == 0?" (rombo - ¿es par?)
   - SI: "suma_pares = suma_pares + digito" (rectángulo)
   - NO: continuar
7. "N = N // 10" (rectángulo - eliminar último dígito)
8. Volver a paso 4
9. "Imprimir suma_pares" (paralelogramo - salida)
10. FIN (óvalo)

LÓGICA MATEMÁTICA:
- N % 10: obtiene el último dígito
- N // 10: elimina el último dígito
- digito % 2 == 0: verifica si es par
- Dígitos pares: 0, 2, 4, 6, 8

PRUEBA DE ESCRITORIO:
====================
Variables clave para Excel:
- N: número (se modifica)
- digito: dígito actual extraído
- es_par: TRUE/FALSE
- suma_pares: acumulador de suma

Ejemplo N=24681:
| N     | digito | es_par | suma_pares | operacion        |
|-------|--------|--------|------------|------------------|
| 24681 | 1      | FALSE  | 0          | -                |
| 2468  | 8      | TRUE   | 8          | 0 + 8 = 8        |
| 246   | 6      | TRUE   | 14         | 8 + 6 = 14       |
| 24    | 4      | TRUE   | 18         | 14 + 4 = 18      |
| 2     | 2      | TRUE   | 20         | 18 + 2 = 20      |
| 0     | -      | -      | 20         | Resultado: 20    |

Ejemplo N=13579:
| N     | digito | es_par | suma_pares | operacion     |
|-------|--------|--------|------------|---------------|
| 13579 | 9      | FALSE  | 0          | -             |
| 1357  | 7      | FALSE  | 0          | -             |
| 135   | 5      | FALSE  | 0          | -             |
| 13    | 3      | FALSE  | 0          | -             |
| 1     | 1      | FALSE  | 0          | -             |
| 0     | -      | -      | 0          | Resultado: 0  |

Ejemplo N=2048:
| N    | digito | es_par | suma_pares | operacion       |
|------|--------|--------|------------|-----------------|
| 2048 | 8      | TRUE   | 8          | 0 + 8 = 8       |
| 204  | 4      | TRUE   | 12         | 8 + 4 = 12      |
| 20   | 0      | TRUE   | 12         | 12 + 0 = 12     |
| 2    | 2      | TRUE   | 14         | 12 + 2 = 14     |
| 0    | -      | -      | 14         | Resultado: 14   |

Ejemplo N=102:
| N   | digito | es_par | suma_pares | operacion     |
|-----|--------|--------|------------|---------------|
| 102 | 2      | TRUE   | 2          | 0 + 2 = 2     |
| 10  | 0      | TRUE   | 2          | 2 + 0 = 2     |
| 1   | 1      | FALSE  | 2          | -             |
| 0   | -      | -      | 2          | Resultado: 2  |
"""

# Ingreso de dato
N = int(input("Ingrese un número: "))

# Inicialización
suma_pares = 0

# Sumar dígitos pares
while N > 0:
    digito = N % 10  # Extraer último dígito
    
    if digito % 2 == 0:  # Verificar si es par
        suma_pares = suma_pares + digito
    
    N = N // 10  # Eliminar último dígito

# Salida
print("Suma de dígitos pares:", suma_pares)
