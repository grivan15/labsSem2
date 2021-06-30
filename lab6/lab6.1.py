from sympy import *
from math import *

N = 10
epsilon = 0.0001


def funct(x):
    return 1 / tan(x) - x


def local(a, b, N):
    x0 = a
    x1 = a + (b - a) / N
    while funct(x0) * funct(x1) >= 0:
        x0 = x1
        x1 += (b - a) / N
        if x1 == b:
            N = 2 * N
            x0 = a
            x1 = a + (b - a) / N
    return {"x0": x0, "x1": x1}


def count_x1(x0):
    return float(x0 - float(funct(x0) / (-(pow(1 / sin(x0), 2) - 1))))


def newt(interval):
    a = interval["x0"]
    b = interval["x1"]
    x0 = float(b)
    x1 = count_x1(x0)
    while abs(x1 - x0) >= epsilon:
        x0 = x1
        x1 = count_x1(x0)
    return x1


a = float(1)
b = float(1.5)
print(f'x = {newt(local(a, b, N))}')