def encontrar_primos(inicio, fin):
    """
    Imprime números primos en un rango dado.
    - inicio: Límite inferior (incluido)
    - fin: Límite superior (incluido)
    """
    print(f"Primos entre {inicio} y {fin}:")
    for num in range(max(2, inicio), fin + 1):  # Comienza desde 2 si inicio < 2
        es_primo = True
        # Optimización: Verificar divisores hasta la raíz cuadrada de num
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                es_primo = False
                break  # No es primo, pasar al siguiente
        if es_primo:
            print(num, end=" ")

encontrar_primos(10, 50)  # Ejemplo: Primos entre 10 y 50