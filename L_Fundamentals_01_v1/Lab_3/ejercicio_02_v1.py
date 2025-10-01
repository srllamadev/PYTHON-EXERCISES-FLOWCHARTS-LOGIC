def fibonacci(n):
    serie = []
    a, b = 0, 1
    for _ in range(n + 1):
        serie.append(a)
        a, b = b, a + b
    return serie

# Leer entradas hasta EOF
try:
    while True:
        n = int(input())
        serie = fibonacci(n)
        print(" ".join(map(str, serie)))

except EOFError:
    pass
