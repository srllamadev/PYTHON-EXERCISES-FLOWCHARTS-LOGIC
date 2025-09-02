'''
Dado N números, calcular la Media Aritmética, 
la Media Armónica, la Media Geométrica y la Media Cuadrática,
mostrando el resultado máximo con dos decimales.
'''
import math

# Leer cantidad de números
N = int(input())

if N <= 0:
    # Si no hay datos, mostrar 0.00 cuatro veces
    print("0.00")
    print("0.00")
    print("0.00")
    print("0.00")
else:
    suma = 0.0
    suma_recip = 0.0
    producto = 1.0
    suma_cuad = 0.0
    
    for _ in range(N):
        x = float(input())
        suma += x
        # acumulación para media armónica
        if x != 0:
            suma_recip += 1.0 / x
        else:
            # si hay cero, la media armónica tiende a 0
            suma_recip = float('inf')
        producto *= x
        suma_cuad += x * x
    
    # Cálculos de medias
    media_arit = suma / N
    media_arm = N / suma_recip if suma_recip not in (0.0, float('inf')) else 0.0
    media_geo = producto ** (1.0 / N) if producto >= 0 else 0.0
    media_cuad = math.sqrt(suma_cuad / N)
    
    # Imprimir cada media con dos decimales
    print(f"{media_arit:.2f}")
    print(f"{media_arm:.2f}")
    print(f"{media_geo:.2f}")
    print(f"{media_cuad:.2f}")