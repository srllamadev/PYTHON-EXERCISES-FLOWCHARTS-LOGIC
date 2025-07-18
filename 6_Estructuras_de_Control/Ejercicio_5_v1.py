def multiplos_comunes(num1, num2, n):
    """
    Imprime los primeros 'n' múltiplos comunes de dos números.
    - num1, num2: Números base
    - n: Cantidad de múltiplos a mostrar
    """
    contador = 0
    multiplo = 0
    
    print(f"\nPrimeros {n} múltiplos comunes de {num1} y {num2}:")
    while contador < n:
        multiplo += 1
        # Verificar si es múltiplo de ambos
        if multiplo % num1 == 0 and multiplo % num2 == 0:
            print(multiplo, end=" ")
            contador += 1

multiplos_comunes(3, 5, 6)  # Ejemplo: Múltiplos de 3 y 5 (15, 30, 45...)