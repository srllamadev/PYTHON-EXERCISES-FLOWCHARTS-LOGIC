def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    serie = [0, 1]
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        serie.append(b)
    return serie

try:
    while True:
        try:
            n = int(input().strip())
            if n < 0:
                print("Por favor ingrese un número entero no negativo.")
                continue
            serie = fibonacci(n)
            print(" ".join(map(str, serie)))
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.")
except EOFError:
    pass