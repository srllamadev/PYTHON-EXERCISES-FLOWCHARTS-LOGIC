from __future__ import annotations
from typing import List

def build_pyramid_powers(n: int) -> List[str]:
    if not (1 <= n <= 10):
        raise ValueError("n debe estar entre 1 y 10")
    lines: List[str] = []
    for i in range(1, n + 1):
        asc = [2 ** k for k in range(i)]
        desc = asc[-2::-1] if i > 1 else []
        row = asc + desc
        lines.append(" ".join(str(x) for x in row))
    return lines
def solve(n: int) -> List[str]:
    """Devuelve las líneas de la pirámide de potencias de 2 para 1..n."""
    return build_pyramid_powers(n)
def demo() -> None:
    print("Ejercicio 01: Pirámide de potencias de 2")
    n = 8
    for line in solve(n):
        print(line)
if __name__ == "__main__":
    demo()
