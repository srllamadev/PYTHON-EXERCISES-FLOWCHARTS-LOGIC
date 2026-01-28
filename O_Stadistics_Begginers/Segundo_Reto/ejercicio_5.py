"""
EJERCICIO 5: Verificar si un número es palíndromo

ANÁLISIS DEL PROBLEMA:
====================
Entrada: 
  - N: número entero positivo

Proceso:
  - Guardar el número original
  - Invertir el número usando operaciones matemáticas
  - Comparar el número original con el invertido
  - Si son iguales, es palíndromo

Salida:
  - Mensaje indicando si el número es o no palíndromo

GUÍA PARA DIAGRAMA DE FLUJO:
============================
1. INICIO (óvalo)
2. "Ingresar N" (paralelogramo - entrada)
3. "numero_original = N" (rectángulo - guardar valor)
4. "numero_invertido = 0" (rectángulo)
5. "¿N > 0?" (rombo - decisión)
   - SI: continuar
   - NO: ir a paso 9
6. "digito = N % 10" (rectángulo)
7. "numero_invertido = numero_invertido * 10 + digito" (rectángulo)
8. "N = N // 10" (rectángulo), volver a paso 5
9. "¿numero_original == numero_invertido?" (rombo - decisión)
   - SI: "Imprimir 'Es palíndromo'" (paralelogramo)
   - NO: "Imprimir 'No es palíndromo'" (paralelogramo)
10. FIN (óvalo)

CONCEPTO DE PALÍNDROMO:
- Un número es palíndromo si se lee igual de izquierda a derecha 
  que de derecha a izquierda
- Ejemplos: 121, 1331, 12321, 9009

PRUEBA DE ESCRITORIO:
====================
Variables clave para Excel:
- N: número ingresado (se modifica)
- numero_original: copia del número original
- digito: dígito actual extraído
- numero_invertido: número reconstruido invertido
- es_palindromo: TRUE/FALSE

Ejemplo N=12321:
| N     | numero_original | digito | numero_invertido | operacion           |
|-------|----------------|--------|------------------|---------------------|
| 12321 | 12321          | -      | 0                | -                   |
| 12321 | 12321          | 1      | 1                | 0*10 + 1 = 1        |
| 1232  | 12321          | 2      | 12               | 1*10 + 2 = 12       |
| 123   | 12321          | 3      | 123              | 12*10 + 3 = 123     |
| 12    | 12321          | 2      | 1232             | 123*10 + 2 = 1232   |
| 1     | 12321          | 1      | 12321            | 1232*10 + 1 = 12321 |
| 0     | 12321          | -      | 12321            | 12321==12321? TRUE  |

Ejemplo N=12345:
| N     | numero_original | digito | numero_invertido | operacion           |
|-------|----------------|--------|------------------|---------------------|
| 12345 | 12345          | -      | 0                | -                   |
| 12345 | 12345          | 5      | 5                | 0*10 + 5 = 5        |
| 1234  | 12345          | 4      | 54               | 5*10 + 4 = 54       |
| 123   | 12345          | 3      | 543              | 54*10 + 3 = 543     |
| 12    | 12345          | 2      | 5432             | 543*10 + 2 = 5432   |
| 1     | 12345          | 1      | 54321            | 5432*10 + 1 = 54321 |
| 0     | 12345          | -      | 54321            | 12345==54321? FALSE |

Ejemplo N=1001:
| N    | numero_original | digito | numero_invertido | operacion         |
|------|----------------|--------|------------------|-------------------|
| 1001 | 1001           | -      | 0                | -                 |
| 1001 | 1001           | 1      | 1                | 0*10 + 1 = 1      |
| 100  | 1001           | 0      | 10               | 1*10 + 0 = 10     |
| 10   | 1001           | 0      | 100              | 10*10 + 0 = 100   |
| 1    | 1001           | 1      | 1001             | 100*10 + 1 = 1001 |
| 0    | 1001           | -      | 1001             | 1001==1001? TRUE  |
"""

# Ingreso de dato
N = int(input("Ingrese un número: "))

# Guardar el número original
numero_original = N

# Invertir el número
numero_invertido = 0
while N > 0:
    digito = N % 10
    numero_invertido = numero_invertido * 10 + digito
    N = N // 10

# Verificar si es palíndromo
if numero_original == numero_invertido:
    print("Es palíndromo")
else:
    print("No es palíndromo")
