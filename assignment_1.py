# sources:
# Question 1: github of the course
# Question 2: https://stackoverflow.com/questions/22721579/sorting-a-nested-ordereddict-by-key-recursively
# Question 3: https://personal.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/
from sympy import *
import numpy as np
from typing import Callable

epsilon = 0.000001
h = 0.0001


# Question 1
def safe_call(func, **kwargs):
    annotation = func.__annotations__
    localvars = locals()
    for key in annotation.keys():
        if annotation[key] is not None and type(kwargs[key]) is not annotation[key]:
            raise TypeError(f'{key} has to be {annotation[key]} but defined as {type(kwargs[key])}.')
    print(func(**kwargs))
    return func(**kwargs)


# Question 2
def print_sorted(arg):
    result = {}
    typeofarg = type(arg)
    for k, v in sorted(arg.items()):
        if isinstance(v, dict):
            result[k] = print_sorted(v)
        else:
            result[k] = v
    return result


# Question 3
def find_root(f, a: float, b: float):
    xn = a
    for i in range(0, 10):
        fxn = f(xn)
        if abs(fxn) < epsilon and a < xn < b:
            print(f'Found solution after {i} iterations.')
            print(xn)
            return xn
        Dfxn = fderivative(f, xn)
        # Dfxn = ftest(f,xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn / Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None


def fderivative(f, xn):
    return (f(xn + h) - f(xn)) / h


if __name__ == '__main__':
    def f1(a: int, b: float, c: int):
        return a + b + c


    safe_call(f1, a=5, b=7.0, c=3)  # should print 15.0
    safe_call(f1, a=10, b=1.0, c=8)  # should print 19.0
    safe_call(f1, a=10, b=10.0, c=3)  # should print 23.0
    print()


    def g(a: int, b: float, c: int, d: float):
        return (a + b + c) * d


    safe_call(g, a=5, b=7.0, c=3, d=2.0)  # should print 30.0
    safe_call(g, a=10, b=1.0, c=8, d=3.0)  # should print 57.0
    safe_call(g, a=10, b=10.0, c=3, d=3.0)  # should print 69.0
    print()


    # c has no annotation and can accept any type of value (int/float...)
    def j(a: int, b: float, c):
        return a * b * c


    safe_call(j, a=5, b=7.0, c=3)  # should print 105.0
    safe_call(j, a=10, b=1.0, c=8)  # should print 80
    safe_call(j, a=10, b=10.0, c=3.0)  # should print 300.0
    safe_call(j, a=5, b=11.0, c=3)  # should print 165.0
    print()


    def l(a: int, b: int, c: int, d: int, e: int, f: int):
        return a + b + c + d + e + f


    safe_call(l, a=5, b=11, c=3, d=10, e=12, f=4)  # should print 45
    safe_call(l, a=3, b=1, c=54, d=12, e=145, f=98)  # should print 313
    safe_call(l, a=1, b=14, c=143, d=1, e=66, f=5)  # should print 230
    print()

    find_root(lambda x: x ** 2 - 4, 1, 3)  # should return 2 (approximately)
    print()
    find_root(lambda x: x ** 3 - x ** 2 - 1, 1, 3)  # should return 1.465 (approximately).
    print()
    find_root(lambda x: x ** (1 / 3), 0, 5)  # should return no solution found
    print()
    find_root(lambda x: x ** 2 - 25, 1, 10)  # should return 5 (approximately)
    print()
    find_root(lambda x: x ** 2 - 49, 1, 10)  # should return 7 (approximately)
    print()

    x = {"a": 5, "c": 6, "b": {1, 3, 2, 4}}
    y = {"c": 12, "a": 333, "b": 76, "d": {4, 3, 2, 1}}
    z = {"h": 10, "f": 20, "i": 13}
    print(print_sorted(x))
    print(print_sorted(y))
    print(print_sorted(z))
