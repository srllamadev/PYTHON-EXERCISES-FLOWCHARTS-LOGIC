from __future__ import annotations
from typing import List, Tuple


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial negativo")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def sin_taylor(x: float, n: int) -> float:
    s = 0.0
    for k in range(n + 1):
        num = x ** (2 * k + 1)
        den = factorial(2 * k + 1)
        term = ((-1.0) ** k) * (num / den)
        s += term
    return s


def cos_taylor(x: float, n: int) -> float:
    s = 0.0
    for k in range(n + 1):
        num = x ** (2 * k)
        den = factorial(2 * k)
        term = ((-1.0) ** k) * (num / den)
        s += term
    return s


def exp_taylor(x: float, n: int) -> float:
    s = 0.0
    for k in range(n + 1):
        num = x ** k
        den = factorial(k)
        s += num / den
    return s


def solve(x: float) -> List[Tuple[int, float, float, float]]:
    rows: List[Tuple[int, float, float, float]] = []
    for n in range(0, 11):
        rows.append((n, sin_taylor(x, n), cos_taylor(x, n), exp_taylor(x, n)))
    return rows


def demo() -> None:
    print("Ejercicio 03: Series de Taylor sin/cos/exp")
    x = 0.5
    print("n  sin(x)        cos(x)        e^x")
    for n, s, c, e in solve(x):
        print(f"{n:02d} {s:.11f} {c:.11f} {e:.11f}")


if __name__ == "__main__":
    demo()
