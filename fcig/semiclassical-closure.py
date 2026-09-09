#!/usr/bin/env python3
"""Sanity checks for FCIG Model XV.

No external dependencies. This is not a proof; it checks sign conventions and the
counterterm bookkeeping used in the note with a finite-dimensional toy model.
"""

from math import isclose, log


def s_grav(x: float, a: float) -> float:
    return 0.5 * a * x * x


def w_matter(x: float, b: float, j: float) -> float:
    return 0.5 * b * x * x - j * x


def s_ct(x: float, c: float) -> float:
    return 0.5 * c * x * x


def d_dx(fun, x: float, h: float = 1e-6) -> float:
    return (fun(x + h) - fun(x - h)) / (2.0 * h)


def check_stationarity_convention() -> None:
    a, b, j = 3.0, 2.0, 5.0
    x_star = j / (a + b)

    e_grav = a * x_star
    t_matter = -(b * x_star - j)
    assert isclose(e_grav, t_matter, rel_tol=0.0, abs_tol=1e-12)

    total_derivative = d_dx(
        lambda x: s_grav(x, a) + w_matter(x, b, j), x_star
    )
    assert abs(total_derivative) < 1e-8


def check_counterterm_transfer() -> None:
    a, b, j, c = 3.0, 2.0, 5.0, 0.7

    old_total = lambda x: s_grav(x, a) + w_matter(x, b, j)
    new_total = lambda x: (
        s_grav(x, a) - s_ct(x, c)
        + w_matter(x, b, j) + s_ct(x, c)
    )

    for x in (-1.3, 0.0, 0.7, 2.1):
        assert isclose(old_total(x), new_total(x), abs_tol=1e-12)
        assert isclose(d_dx(old_total, x), d_dx(new_total, x), abs_tol=1e-8)


def check_state_count_scaling_warning() -> None:
    # FCIG capacity entropy in the asymptotic model scales logarithmically in k.
    # This check only makes the contrast with an area-linear law explicit.
    d = 2
    k1, k2 = 10.0, 100.0
    delta_s_cap = d * (log(k2) - log(k1))
    assert isclose(delta_s_cap, d * log(10.0), abs_tol=1e-12)

    # There is no canonical area variable in this expression: introducing one
    # requires extra structure, exactly as stated in Model XV.


def main() -> None:
    check_stationarity_convention()
    check_counterterm_transfer()
    check_state_count_scaling_warning()
    print("Model XV sanity checks: PASS")


if __name__ == "__main__":
    main()
