#el codigo trata de calcular una sumatoria basada en dos series
#la primera serie es la suma de 2/k para k desde 1 hasta n
#la segunda serie es una suma alternada de potencias de x divididas por factoriales
#la salida es el resultado de la suma de ambas series
#la funcion recibe n y x como parametros
#y devuelve el resultado de la sumatoria
import math

def calcular_sumatoria(n, x):
    suma1 = sum(2 / k for k in range(1, n + 1))
    suma2 = sum(((-1) ** i / math.factorial(2 + i)) * (x ** (2 + i)) for i in range(1, n + 1))
    return suma1 + suma2

# Solicitar datos al usuario
n = int(input("Ingrese el valor de n: "))
x = float(input("Ingrese el valor de x: "))

# Calcular la sumatoria
resultado = calcular_sumatoria(n, x)

# Mostrar resultado
print("El resultado de la sumatoria es:", resultado)
