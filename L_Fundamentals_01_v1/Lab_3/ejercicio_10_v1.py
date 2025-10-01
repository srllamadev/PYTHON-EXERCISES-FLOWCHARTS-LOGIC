from __future__ import annotations
from typing import List, Tuple


def combinations_1_to_7() -> List[Tuple[int, int]]:
    pairs: List[Tuple[int, int]] = []
    for i in range(1, 8):
        for j in range(i + 1, 8):
            pairs.append((i, j))
    return pairs


def midpoint(a: Tuple[float, float], b: Tuple[float, float]) -> Tuple[float, float]:
    return ((a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0)


def solve() -> dict:
    return {
        "pairs": combinations_1_to_7(),
        "midpoints": [
            ((0, 0), (2, 1), midpoint((0, 0), (2, 1))),
            ((1, 4), (4, 2), midpoint((1, 4), (4, 2))),
            ((2, 8), (8, 3), midpoint((2, 8), (8, 3))),
            ((3, 12), (16, 4), midpoint((3, 12), (16, 4))),
            ((4, 16), (32, 5), midpoint((4, 16), (32, 5))),
        ],
    }


def demo() -> None:
    print("Ejercicio 07: combinaciones y tabla de puntos medios")
    pairs = combinations_1_to_7()
    for p in pairs:
        print(p)
    print(f"\nEl número total de todas las combinaciones es {len(pairs)}")

if __name__ == "__main__":
    demo()
