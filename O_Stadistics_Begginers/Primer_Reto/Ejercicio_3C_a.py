##Dados N números, encontrar el máximo y el mínimo de los datos leídos. Leer cantidad de números
N = int(input())

# Si no hay datos, mostrar 0 0
if N <= 0:
    print(0, 0)
else:
    # Leer lista de números
    nums = [int(input()) for _ in range(N)]
    # Calcular máximo y mínimo
    max_val = max(nums)
    min_val = min(nums)
    # Imprimir resultados
    print(max_val)
    print(min_val)