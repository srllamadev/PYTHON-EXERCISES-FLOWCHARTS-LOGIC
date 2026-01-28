import math

# Leer cantidad de números
N = int(input())

# Acumular suma de los números
total = 0.0
for _ in range(N):
    x = float(input())
    total += x

# Calcular raíz cuadrada de la suma (considera sumas negativas no permitidas)
resultado = math.sqrt(total) if total >= 0 else 0.0
print(round(resultado,2))