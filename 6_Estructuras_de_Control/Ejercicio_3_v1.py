def triangulo_numerico(niveles):
    """
    Imprime un patrón de triángulo invertido:
    1 2 3 4
    1 2 3
    1 2
    1
    """
    print(f"\nTriángulo numérico ({niveles} niveles):")
    for i in range(niveles, 0, -1):  # De niveles a 1 (paso -1)
        # Imprimir números desde 1 hasta i
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # Nueva línea

triangulo_numerico(5)  # Ejemplo con 5 niveles