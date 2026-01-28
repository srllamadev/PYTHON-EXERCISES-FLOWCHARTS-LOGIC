"""
EJERCICIO 2: Hallar el MCD mediante el Algoritmo de Euclides

ANÁLISIS DEL PROBLEMA:
====================
Entrada: 
  - a: primer número entero positivo
  - b: segundo número entero positivo

Proceso:
  - Aplicar el Algoritmo de Euclides:
    * Mientras b sea diferente de 0:
      - Calcular residuo = a % b
      - Actualizar a = b
      - Actualizar b = residuo
    * El MCD es el valor final de a

Salida:
  - MCD: Máximo Común Divisor de los dos números

GUÍA PARA DIAGRAMA DE FLUJO:
============================
1. INICIO (óvalo)
2. "Ingresar a, b" (paralelogramo - entrada)
3. "¿b != 0?" (rombo - decisión)
   - SI: continuar
   - NO: ir a paso 7
4. "residuo = a % b" (rectángulo - proceso)
5. "a = b" (rectángulo)
6. "b = residuo" (rectángulo), volver a paso 3
7. "Imprimir 'MCD:', a" (paralelogramo - salida)
8. FIN (óvalo)

ALGORITMO DE EUCLIDES:
- Se basa en que MCD(a,b) = MCD(b, a%b)
- Se repite hasta que b = 0
- El último valor de a es el MCD

PRUEBA DE ESCRITORIO:
====================
Variables clave para Excel:
- a: primer número (se actualiza)
- b: segundo número (se actualiza)
- residuo: a % b
- iteracion: contador de iteraciones

Ejemplo a=48, b=18:
| iteracion | a  | b  | residuo | b!=0  |
|-----------|----|----|---------|-------|
| 0         | 48 | 18 | -       | TRUE  |
| 1         | 18 | 12 | 12      | TRUE  |
| 2         | 12 | 6  | 6       | TRUE  |
| 3         | 6  | 0  | 0       | FALSE |
| Resultado | 6  | 0  | -       | MCD=6 |

Ejemplo a=56, b=98:
| iteracion | a  | b  | residuo | b!=0  |
|-----------|----|----|---------|-------|
| 0         | 56 | 98 | -       | TRUE  |
| 1         | 98 | 56 | 56      | TRUE  |
| 2         | 56 | 42 | 42      | TRUE  |
| 3         | 42 | 14 | 14      | TRUE  |
| 4         | 14 | 0  | 0       | FALSE |
| Resultado | 14 | 0  | -       | MCD=14|
"""

# Ingreso de datos
a = int(input("Ingrese primer número: "))
b = int(input("Ingrese segundo número: "))

# Algoritmo de Euclides
while b != 0:
    residuo = a % b
    a = b
    b = residuo

# Salida
print("MCD:", a)
