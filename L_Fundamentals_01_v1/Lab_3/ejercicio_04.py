from __future__ import annotations
from math import sqrt
from typing import Iterable, Tuple


def mean(values: Iterable[float]) -> float:
    vals = list(values)
    if not vals:
        return 0.0
    return sum(vals) / len(vals)


def stddev(values: Iterable[float]) -> float:
    vals = list(values)
    if not vals:
        return 0.0
    m = mean(vals)
    n = len(vals)
    if n <= 1:
        return 0.0
    var = sum((x - m) ** 2 for x in vals) / (n - 1)
    return sqrt(var)


def solve(nums: Iterable[float]) -> Tuple[float, float]:
    m = mean(nums)
    s = stddev(nums)
    return m, s


def demo() -> None:
    print("Ejercicio 04: media y desviación estándar")
    datos = [1, 2, 3, 4.5, 5.6, 6, 7, 8, 9, 10]
    m, s = solve(datos)
    print(f"La media es {m:.2f}")
    print(f"La desviación estándar es {s:.5f}")


if __name__ == "__main__":
    demo()
