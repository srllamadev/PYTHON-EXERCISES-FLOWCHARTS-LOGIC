"""
EJERCICIO 6: Producto de dos números mediante sumas sucesivas

ANÁLISIS DEL PROBLEMA:
====================
Entrada: 
  - a: primer número entero
  - b: segundo número entero

Proceso:
  - Multiplicar es sumar un número tantas veces como indica el otro
  - Ejemplo: 5 × 3 = 5 + 5 + 5 = 15
  - Sumar 'a' consecutivamente 'b' veces
  - Manejar casos negativos

Salida:
  - producto: resultado de la multiplicación

GUÍA PARA DIAGRAMA DE FLUJO:
============================
1. INICIO (óvalo)
2. "Ingresar a, b" (paralelogramo - entrada)
3. "producto = 0" (rectángulo)
4. "contador = 0" (rectángulo)
5. "¿contador < b?" (rombo - decisión)
   - SI: continuar
   - NO: ir a paso 8
6. "producto = producto + a" (rectángulo)
7. "contador = contador + 1" (rectángulo), volver a paso 5
8. "Imprimir producto" (paralelogramo - salida)
9. FIN (óvalo)

ALTERNATIVA CON WHILE:
1. INICIO (óvalo)
2. "Ingresar a, b" (paralelogramo)
3. "producto = 0" (rectángulo)
4. "veces = b" (rectángulo)
5. "¿veces > 0?" (rombo)
   - SI: continuar
   - NO: ir a paso 8
6. "producto = producto + a" (rectángulo)
7. "veces = veces - 1" (rectángulo), volver a paso 5
8. "Imprimir producto" (paralelogramo)
9. FIN (óvalo)

LÓGICA MATEMÁTICA:
- Multiplicación como suma repetida: a × b = a + a + a + ... (b veces)
- Ejemplo: 7 × 4 = 7 + 7 + 7 + 7 = 28

PRUEBA DE ESCRITORIO:
====================
Variables clave para Excel:
- a: número a sumar
- b: cantidad de veces a sumar
- producto: acumulador del resultado
- contador: control de iteraciones

Ejemplo a=6, b=4:
| contador | producto | operacion       | contador < b |
|----------|----------|-----------------|--------------|
| 0        | 0        | -               | TRUE         |
| 1        | 6        | 0 + 6 = 6       | TRUE         |
| 2        | 12       | 6 + 6 = 12      | TRUE         |
| 3        | 18       | 12 + 6 = 18     | TRUE         |
| 4        | 24       | 18 + 6 = 24     | FALSE        |
| Resultado: 6 × 4 = 24                                |

Ejemplo a=8, b=5:
| contador | producto | operacion       | contador < b |
|----------|----------|-----------------|--------------|
| 0        | 0        | -               | TRUE         |
| 1        | 8        | 0 + 8 = 8       | TRUE         |
| 2        | 16       | 8 + 8 = 16      | TRUE         |
| 3        | 24       | 16 + 8 = 24     | TRUE         |
| 4        | 32       | 24 + 8 = 32     | TRUE         |
| 5        | 40       | 32 + 8 = 40     | FALSE        |
| Resultado: 8 × 5 = 40                                |

Ejemplo a=12, b=3:
| contador | producto | operacion       | contador < b |
|----------|----------|-----------------|--------------|
| 0        | 0        | -               | TRUE         |
| 1        | 12       | 0 + 12 = 12     | TRUE         |
| 2        | 24       | 12 + 12 = 24    | TRUE         |
| 3        | 36       | 24 + 12 = 36    | FALSE        |
| Resultado: 12 × 3 = 36                               |
"""

# Ingreso de datos
a = int(input("Ingrese primer número: "))
b = int(input("Ingrese segundo número: "))

# Inicialización
producto = 0
contador = 0

# Multiplicación por sumas sucesivas
while contador < b:
    producto = producto + a
    contador = contador + 1

# Salida
print("Producto:", producto)
