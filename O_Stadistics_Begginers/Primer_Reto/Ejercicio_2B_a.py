# Leer cantidad de números
N = int(input())

# Si no hay números, el rango es 0
if N <= 0:
    print(0)
else:
    # Leer todos los números
    nums = [int(input()) for _ in range(N)]
    # Calcular rango
    rango = max(nums) - min(nums)
    print(rango)