from __future__ import annotations
from typing import List, Tuple


def monthly_payment(P: float, annual_rate_percent: float, years: int) -> float:
    r = (annual_rate_percent / 100.0) / 12.0
    n = years * 12
    if r == 0:
        return P / n
    return P * r / (1.0 - (1.0 + r) ** (-n))


def solve(principal: float, years: int) -> List[Tuple[float, float, float]]:
    """Devuelve lista de (tasa%, pagoMensual, pagoTotal) para tasas 5%..8% step 0.125%."""
    results: List[Tuple[float, float, float]] = []
    rate = 5.0
    while rate <= 8.0 + 1e-9:
        m = monthly_payment(principal, rate, years)
        total = m * years * 12
        results.append((rate, m, total))
        rate += 0.125
        rate = round(rate, 3)  # evitar arrastre binario
    return results


def demo() -> None:
    print("Ejercicio 06: tabla de pagos de préstamo")
    principal = 10000.0
    years = 5
    print("Tasa de interés | Pago mensual | Pago total")
    for rate, m, t in solve(principal, years):
        print(f"{rate:>6.3f}%          | {m:>7.2f}       | {t:>8.2f}")


if __name__ == "__main__":
    demo()
