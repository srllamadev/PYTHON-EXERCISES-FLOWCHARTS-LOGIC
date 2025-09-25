from __future__ import annotations
from typing import Iterator, List


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    p = 3
    while p * p <= num:
        if num % p == 0:
            return False
        p += 2
    return True


def primes_in_range(a: int, b: int) -> List[int]:
    return [x for x in range(max(2, a), b + 1) if is_prime(x)]


def fib_sequence() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def nth_prime_fib(n: int) -> int:
    count = 0
    for f in fib_sequence():
        if f > 1 and is_prime(f):
            count += 1
            if count == n:
                return f
        # Evitar ciclos extremos
        if f > 10**10:
            raise ValueError("n demasiado grande para este demo")
    raise RuntimeError("No alcanzable")


def solve_part_a() -> List[str]:
    primes = primes_in_range(2, 1000)
    lines: List[str] = []
    for i in range(0, len(primes), 10):
        lines.append(" ".join(str(x) for x in primes[i:i + 10]))
    return lines


def solve_part_b(inputs: List[int]) -> List[int]:
    return [nth_prime_fib(n) for n in inputs]


def demo() -> None:
    print("Ejercicio 02 - Parte A: Primos 2..1000 (10 por línea)")
    for line in solve_part_a():
        print(line)

    print("\nEjercicio 02 - Parte B: n-ésimo Fibonacci primo")
    data = [1, 2, 3, 4]
    print("Entrada:", data)
    print("Salida:", solve_part_b(data))


if __name__ == "__main__":
    demo()
