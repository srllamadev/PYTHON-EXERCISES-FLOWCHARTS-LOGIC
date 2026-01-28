"""
EJERCICIO 10: Sumar todos los dígitos de un número mayor a cero

ANÁLISIS DEL PROBLEMA:
====================
Entrada: 
  - N: número entero positivo (mayor a cero)

Proceso:
  - Extraer cada dígito del número usando módulo 10
  - Sumar todos los dígitos extraídos
  - Eliminar el dígito procesado con división entera
  - Repetir hasta procesar todos los dígitos

Salida:
  - suma_digitos: suma total de todos los dígitos

GUÍA PARA DIAGRAMA DE FLUJO:
============================
1. INICIO (óvalo)
2. "Ingresar N" (paralelogramo - entrada)
3. "suma_digitos = 0" (rectángulo)
4. "¿N > 0?" (rombo - decisión)
   - SI: continuar
   - NO: ir a paso 8
5. "digito = N % 10" (rectángulo - extraer último dígito)
6. "suma_digitos = suma_digitos + digito" (rectángulo)
7. "N = N // 10" (rectángulo - eliminar último dígito), volver a paso 4
8. "Imprimir suma_digitos" (paralelogramo - salida)
9. FIN (óvalo)

LÓGICA MATEMÁTICA:
- N % 10: obtiene el último dígito
- N // 10: elimina el último dígito
- Sumar todos los dígitos extraídos

Ejemplo: N = 23 → suma = 2 + 3 = 5
Ejemplo: N = 456 → suma = 4 + 5 + 6 = 15

PRUEBA DE ESCRITORIO:
====================
Variables clave para Excel:
- N: número (se modifica)
- digito: dígito actual extraído
- suma_digitos: acumulador de suma
- operacion: cálculo realizado

Ejemplo N=23:
| N  | digito | suma_digitos | operacion    |
|----|--------|--------------|--------------|
| 23 | 3      | 3            | 0 + 3 = 3    |
| 2  | 2      | 5            | 3 + 2 = 5    |
| 0  | -      | 5            | Resultado: 5 |

Ejemplo N=456:
| N   | digito | suma_digitos | operacion     |
|-----|--------|--------------|---------------|
| 456 | 6      | 6            | 0 + 6 = 6     |
| 45  | 5      | 11           | 6 + 5 = 11    |
| 4   | 4      | 15           | 11 + 4 = 15   |
| 0   | -      | 15           | Resultado: 15 |

Ejemplo N=12345:
| N     | digito | suma_digitos | operacion      |
|-------|--------|--------------|----------------|
| 12345 | 5      | 5            | 0 + 5 = 5      |
| 1234  | 4      | 9            | 5 + 4 = 9      |
| 123   | 3      | 12           | 9 + 3 = 12     |
| 12    | 2      | 14           | 12 + 2 = 14    |
| 1     | 1      | 15           | 14 + 1 = 15    |
| 0     | -      | 15           | Resultado: 15  |

Ejemplo N=9876:
| N    | digito | suma_digitos | operacion      |
|------|--------|--------------|----------------|
| 9876 | 6      | 6            | 0 + 6 = 6      |
| 987  | 7      | 13           | 6 + 7 = 13     |
| 98   | 8      | 21           | 13 + 8 = 21    |
| 9    | 9      | 30           | 21 + 9 = 30    |
| 0    | -      | 30           | Resultado: 30  |

Ejemplo N=1000:
| N    | digito | suma_digitos | operacion    |
|------|--------|--------------|--------------|
| 1000 | 0      | 0            | 0 + 0 = 0    |
| 100  | 0      | 0            | 0 + 0 = 0    |
| 10   | 0      | 0            | 0 + 0 = 0    |
| 1    | 1      | 1            | 0 + 1 = 1    |
| 0    | -      | 1            | Resultado: 1 |
"""

# Ingreso de dato
N = int(input("Ingrese un número: "))

# Inicialización
suma_digitos = 0

# Sumar todos los dígitos
while N > 0:
    digito = N % 10  # Extraer último dígito
    suma_digitos = suma_digitos + digito  # Sumar al acumulador
    N = N // 10  # Eliminar último dígito

# Salida
print("Suma de los dígitos:", suma_digitos)
