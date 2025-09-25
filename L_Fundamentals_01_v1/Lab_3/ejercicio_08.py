from __future__ import annotations
from typing import List


def pyramid_numbers(n: int) -> List[str]:
    if not (1 <= n <= 15):
        raise ValueError("n debe estar entre 1 y 15")
    lines: List[str] = []
    width = 2 * n - 1  # número total de números en la última fila si sin espacios
    for i in range(1, n + 1):
        left = list(range(i, 0, -1))
        right = list(range(2, i + 1))
        nums = left + right
        text = " ".join(str(x) for x in nums)
        # centrado simple con espacios a la izquierda (proporcional a n - i)
        pad = "  " * (n - i)
        lines.append(pad + text)
    return lines


def solve(n: int) -> List[str]:
    return pyramid_numbers(n)


def demo() -> None:
    print("Ejercicio 08: pirámide de números")
    n = 7
    for line in solve(n):
        print(line)


if __name__ == "__main__":
    demo()
