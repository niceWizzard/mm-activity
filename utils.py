import numpy as np
from numpy.polynomial import Polynomial

def solve_lagrange(x_val : list[float], y_val: list[float]) -> Polynomial:
    poly_coef = [0 for i in range(len(x_val))]
    for i, (x,y) in enumerate(zip(x_val, y_val)):
        denom = np.prod(x - x_val[x_val != x])
        coef = np.poly(x_val[x_val != x])
        print(f"L{i} =   ({Polynomial(coef=coef[::-1])}) / ({denom :.5f})")
        poly_coef = poly_coef + (y / denom) * coef
    return Polynomial(coef=poly_coef[::-1])

def divided_diff(x_vals: list[float], y_vals: list[float]) -> list[list[float]]:
    n = len(x_vals)
    if n != len(y_vals):
        raise ValueError("x_vals and y_vals must have the same length.")

    output: list[list[float]] = []
    prev_row = y_vals[:]

    for level in range(1, n):
        current_row = []
        should_stop = False
        for i in range(n - level):
            numerator = prev_row[i + 1] - prev_row[i]
            denominator = x_vals[i + level] - x_vals[i]
            value = numerator / denominator
            if value <= 0:
                should_stop = True
            current_row.append(value)
        output.append(current_row)
        prev_row = current_row
        if should_stop:
            return output

    return output


def cubic_coef(a: float, b : float, c: float) -> list[float]:
    return [1, -(a+b+c), (a*b + a*c + b*c), -(a*b*c)]


def lagr_denom(x: list[int]) -> list[float]:
    x = np.array(x, dtype=np.float64)
    return [np.prod(main - x[x != main]) for main in x]

            