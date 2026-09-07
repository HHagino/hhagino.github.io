"""Numerical sanity checks for FCIG Explicit Model IV.

This script does NOT prove the exact hyperbolic Bergman formula. That theorem is
cited in `hyperbolic-model.md`. It checks algebraic consequences used in the note:

1. the local factor (2k-1)/(4pi) integrates to the Riemann--Roch dimension;
2. supplied geodesic-loop terms are exponentially suppressed in k;
3. the Mumford exponent 6k^2-6k+1 is not proportional to rank/2.

Dependency: Python standard library only.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class LoopDatum:
    length: float
    holonomy_phase: float = 0.0  # alpha in exp(2 pi i alpha)


def hyperbolic_area(genus: int) -> float:
    if genus < 2:
        raise ValueError("genus must be at least 2")
    return 4.0 * math.pi * (genus - 1)


def rr_rank(genus: int, k: int) -> int:
    if genus < 2 or k < 2:
        raise ValueError("require genus >= 2 and k >= 2")
    return (2 * k - 1) * (genus - 1)


def local_density(k: int) -> float:
    if k < 2:
        raise ValueError("require k >= 2")
    return (2 * k - 1) / (4.0 * math.pi)


def loop_factor(k: int, loops: list[LoopDatum]) -> float:
    """Finite truncation of Sun's geodesic-loop correction factor."""
    total = 0.0
    for loop in loops:
        amp = math.cosh(loop.length / 2.0) ** (-2 * k)
        phase = math.cos(2.0 * math.pi * k * loop.holonomy_phase)
        total += amp * phase
    return total


def truncated_density(k: int, loops: list[LoopDatum]) -> float:
    return local_density(k) * (1.0 + loop_factor(k, loops))


def mumford_exponent(k: int) -> int:
    return 6 * k * k - 6 * k + 1


def run_demo() -> None:
    print("FCIG Explicit Model IV: hyperbolic local/global sanity checks")
    print()

    print("[1] Riemann--Roch normalization")
    for genus in (2, 3, 5):
        for k in (2, 3, 5):
            integrated_local = local_density(k) * hyperbolic_area(genus)
            expected = rr_rank(genus, k)
            err = abs(integrated_local - expected)
            print(
                f"g={genus}, k={k}: local integral={integrated_local:.12f}, "
                f"rank={expected}, error={err:.3e}"
            )
    print()

    # A finite illustrative loop list. These are not claimed to be a complete
    # spectrum of any chosen compact surface. The purpose is only to display
    # the exact suppression factor appearing in the cited formula.
    loops = [
        LoopDatum(length=3.0, holonomy_phase=0.0),
        LoopDatum(length=4.2, holonomy_phase=0.125),
        LoopDatum(length=5.1, holonomy_phase=0.0),
    ]

    print("[2] Finite geodesic-loop truncation")
    previous = None
    for k in range(2, 9):
        correction = loop_factor(k, loops)
        density = truncated_density(k, loops)
        ratio = abs(correction / previous) if previous not in (None, 0.0) else float("nan")
        print(
            f"k={k}: loop correction={correction:+.6e}, "
            f"truncated density={density:.12f}, ratio={ratio:.6f}"
        )
        previous = correction
    print()

    print("[3] Rank/2 versus Mumford exponent (genus 2)")
    for k in range(2, 8):
        half_rank = rr_rank(2, k) / 2.0
        ck = mumford_exponent(k)
        print(
            f"k={k}: rank/2={half_rank:5.1f}, "
            f"Mumford exponent={ck:4d}, ratio={ck / half_rank:8.3f}"
        )


if __name__ == "__main__":
    run_demo()
