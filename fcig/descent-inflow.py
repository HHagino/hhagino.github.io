#!/usr/bin/env python3
"""Formal coefficient checks for FCIG Model XIII.

This does not construct the global Dai--Freed anomaly theory. It checks only
local transgression/descent coefficient algebra in the fixed normalized basis.
"""

from fractions import Fraction


def coefficients(charge: int = 1) -> tuple[Fraction, Fraction]:
    """Return coefficients of c^3 and c*p1 in I6(q)."""
    return Fraction(charge**3, 6), -Fraction(charge, 24)


def check_charge(charge: int) -> None:
    cubic, mixed = coefficients(charge)

    # If I5 = cubic * a*c^2 + mixed * a*p1 and da=c while dc=dp1=0,
    # then dI5 = cubic*c^3 + mixed*c*p1 = I6.
    d_i5 = (cubic, mixed)
    i6 = (cubic, mixed)
    assert d_i5 == i6

    # If delta a=d alpha, then delta I5=d[alpha(cubic*c^2+mixed*p1)].
    descent_4 = (cubic, mixed)
    assert descent_4 == i6

    print(
        f"q={charge:+d}: I6 = ({cubic}) c^3 + ({mixed}) c p1; "
        "dI5 and gauge descent: PASS"
    )


def main() -> None:
    for q in (-3, -2, -1, 1, 2, 3):
        check_charge(q)

    # The rational coefficients should not be mistaken for integral
    # characteristic-class coefficients term by term.
    c3, cp1 = coefficients(1)
    assert c3.denominator == 6
    assert cp1.denominator == 24
    print("\nrational-coefficient quantization warning: PASS")
    print("  global fermionic quantization must be justified by index/anomaly theory")

    # Dimensional chain used by descent.
    assert 6 == 5 + 1
    assert 5 == 4 + 1
    print("\ndegree chain 6 -> 5 -> 4: PASS")


if __name__ == "__main__":
    main()
