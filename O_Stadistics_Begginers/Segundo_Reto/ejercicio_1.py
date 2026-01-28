"""
EJERCICIO 1: Imprimir números primos y su suma hasta un número N

ANÁLISIS DEL PROBLEMA:
====================
Entrada: 
  - N: número entero positivo hasta donde buscar primos

Proceso:
  - Para cada número desde 2 hasta N:
    * Verificar si es primo (divisible solo por 1 y sí mismo)
    * Si es primo, agregarlo a la lista y sumarlo
  - Imprimir los primos encontrados y la suma total

Salida:
  - Lista de números primos hasta N
  - Suma de todos los primos encontrados

GUÍA PARA DIAGRAMA DE FLUJO:
============================
1. INICIO (óvalo)
2. "Ingresar N" (paralelogramo - entrada)
3. "suma_primos = 0" (rectángulo - proceso)
4. "numero = 2" (rectángulo - proceso)
5. "¿numero <= N?" (rombo - decisión)
   - SI: continuar
   - NO: ir a paso 14
6. "contador_divisores = 0" (rectángulo)
7. "divisor = 1" (rectángulo)
8. "¿divisor <= numero?" (rombo)
   - SI: continuar
   - NO: ir a paso 11
9. "¿numero % divisor == 0?" (rombo)
   - SI: "contador_divisores = contador_divisores + 1"
   - NO: continuar
10. "divisor = divisor + 1", volver a paso 8
11. "¿contador_divisores == 2?" (rombo - es primo)
    - SI: "Imprimir numero", "suma_primos = suma_primos + numero"
    - NO: continuar
12. "numero = numero + 1" (rectángulo)
13. Volver a paso 5
14. "Imprimir suma_primos" (paralelogramo - salida)
15. FIN (óvalo)

PRUEBA DE ESCRITORIO:
====================
Variables clave para Excel:
- N: número límite
- numero: número actual evaluando
- divisor: divisor actual
- contador_divisores: cantidad de divisores encontrados
- es_primo: bandera (TRUE/FALSE)
- suma_primos: acumulador de la suma
- primos_encontrados: lista de primos (separados por comas)

Ejemplo N=10:
| numero | divisor | contador_divisores | es_primo | suma_primos | primos_encontrados |
|--------|---------|-------------------|----------|-------------|-------------------|
| 2      | 1..2    | 2                 | TRUE     | 2           | 2                 |
| 3      | 1..3    | 2                 | TRUE     | 5           | 2,3               |
| 4      | 1..4    | 3                 | FALSE    | 5           | 2,3               |
| 5      | 1..5    | 2                 | TRUE     | 10          | 2,3,5             |
| 6      | 1..6    | 4                 | FALSE    | 10          | 2,3,5             |
| 7      | 1..7    | 2                 | TRUE     | 17          | 2,3,5,7           |
| 8      | 1..8    | 4                 | FALSE    | 17          | 2,3,5,7           |
| 9      | 1..9    | 3                 | FALSE    | 17          | 2,3,5,7           |
| 10     | 1..10   | 4                 | FALSE    | 17          | 2,3,5,7           |
"""

# Ingreso de dato
N = int(input("Ingrese N: "))

# Inicialización
suma_primos = 0
primos = []

# Recorrer números desde 2 hasta N
numero = 2
while numero <= N:
    # Contar divisores del número actual
    contador_divisores = 0
    divisor = 1
    
    while divisor <= numero:
        if numero % divisor == 0:
            contador_divisores += 1
        divisor += 1
    
    # Si tiene exactamente 2 divisores, es primo
    if contador_divisores == 2:
        primos.append(numero)
        suma_primos += numero
    
    numero += 1

# Salida
print("Primos:", ", ".join(map(str, primos)))
print("Suma:", suma_primos)
