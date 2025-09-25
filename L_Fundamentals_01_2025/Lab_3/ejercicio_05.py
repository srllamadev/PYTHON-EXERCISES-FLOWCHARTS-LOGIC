from __future__ import annotations
from typing import Tuple


def cantor_term(n: int) -> Tuple[int, int]:
    """Retorna (p, q) del término n (1-indexado) en la enumeración de Cantor.
    Diagonalización por sumas constantes: 1/1, 1/2, 2/1, 3/1, 2/2, 1/3, ...
    """
    if n <= 0:
        raise ValueError("n debe ser >= 1")
    # Encontrar diagonal d tal que d(d+1)/2 >= n
    d = 1
    while d * (d + 1) // 2 < n:
        d += 1
    prev = (d - 1) * d // 2
    idx = n - prev  # posición dentro de la diagonal (1..d)
    if d % 2 == 0:
        # diagonal par: recorre de (1,d) a (d,1)
        p = idx
        q = d - idx + 1
    else:
        # diagonal impar: recorre de (d,1) a (1,d)
        p = d - idx + 1
        q = idx
    return p, q


def solve(n_values):
    return [cantor_term(n) for n in n_values]


def demo() -> None:
    print("Ejercicio 05: Sucesión de Cantor")
    entradas = [3, 14, 7]
    for n in entradas:
        p, q = cantor_term(n)
        print(f"{p}/{q}")


if __name__ == "__main__":
    demo()
