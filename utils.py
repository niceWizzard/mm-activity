import numpy as np
from numpy.polynomial import Polynomial

def solve_lagrange(x_val : list[float], y_val: list[float]) -> Polynomial:
    poly_coef = [0 for i in range(len(x_val))]
    for i, (x,y) in enumerate(zip(x_val, y_val)):
        denom = np.prod(x - x_val[x_val != x])
        coef = np.poly(x_val[x_val != x])
        print(f"L{i} = ({1/denom :.5f})  * ({Polynomial(coef=coef[::-1])})")
        poly_coef = np.sum(
            np.vstack([
                poly_coef,
                (y / denom) * coef,
            ]), 
            axis=0
        )
    return Polynomial(coef=poly_coef[::-1])


def cubic_coef(a: float, b : float, c: float) -> list[float]:
    return [1, -(a+b+c), (a*b + a*c + b*c), -(a*b*c)]


def lagr_denom(x: list[int]) -> list[float]:
    x = np.array(x, dtype=np.float64)
    return [np.prod(main - x[x != main]) for main in x]

            