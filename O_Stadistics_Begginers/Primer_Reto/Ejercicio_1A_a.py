## Programa que calcula el promedio de N numeros

N = int(input()) #ingreso de dato
suma = 0  # inicializa la suma antes del bucle
for _ in range(N): #bucle for
    x = int(input()) #ingreso de dato
    suma += x  # suma de los numeros
print(suma/N) #imprime el promedio