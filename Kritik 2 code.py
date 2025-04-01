import numpy as np


def funny(x):
    if x <= -1:
        return 0
    elif x >= 1:
        return 0
    else:
        return np.exp(1 - (1 / (1 - x ** (10 ** 250))))


def roots(f, a, b, tol=1e-10):
    if f(a) * f(b) > 0:
        return "No root found in given interval"

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2



def f1(x):
    return np.exp(x) + np.log(x)


def f2(x):
    return np.arctan(x) - x ** 2


def f3(x):
    return np.sin(x) / np.log(x)


def f4(x):
    return np.log(np.cos(x))



print("Root of f1 on [0,1]:", roots(f1, 0.1, 1))  # Avoid log(0)
print("Root of f2 on [0,2]:", roots(f2, 0, 2))
print("Root of f3 on [3,4]:", roots(f3, 3, 4))
print("Root of f4 on [5,7]:", roots(f4, 5, 7))
