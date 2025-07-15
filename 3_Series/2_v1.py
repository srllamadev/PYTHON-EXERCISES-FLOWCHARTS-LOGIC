# Generar una sucesión de números según el patrón especificado
# La sucesión sigue el patrón: 2+k, 1+k, k para k = 1, 2, 3, ...
# donde k es el número de grupo y cada grupo tiene 3 números.
# Por ejemplo, el primer grupo es (2+1, 1+1, 1) = (3, 2, 1),
# el segundo grupo es (2+2, 1+2, 2) = (4, 3, 2),
# y así sucesivamente.
# La función genera los primeros n términos de esta sucesión.
def generar_sucesion(n):
    secuencia = []
    for i in range(n):
        # Calcular el índice de grupo (comenzando en 1)
        k = (i // 3) + 1
        
        # Posición dentro del grupo (0, 1 o 2)
        pos = i % 3
        
        if pos == 0:
            valor = 2 + k
        elif pos == 1:
            valor = 1 + k
        else:  # pos == 2
            valor = k
        
        secuencia.append(valor)
    
    return secuencia

# Ejemplo: generar los primeros 15 términos
n = 15
resultado = generar_sucesion(n)
print(resultado)
