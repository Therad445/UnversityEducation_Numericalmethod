import numpy as np
import math


def simp(f, x):
    return (x[-1] - x[0]) / (3 * (len(x) - 1)) * (f(x[0]) + f(x[-1])
                                                  + 2 * sum([f(x[i]) for i in range(2, len(x) - 1, 2)])
                                                  + 4 * sum([f(x[i]) for i in range(1, len(x) - 1, 2)]))


def trap(f, x):
    return (x[1] - x[0]) * ((f(x[0]) + f(x[-1])) / 2
                            + sum([f(x[i]) for i in range(1, len(x) - 1)]))


def show_res(res, s, t):
    s, t = round(s, 4), round(t, 4)
    diff = len(str(s)) - len(str(t))
    print(f'Simpson method: \t{str(s) + " " * max(-diff, 0)}, \t\tdelta = {res - s}')
    print(f'trapezoids method: \t{str(t) + " " * max(diff, 0)}, \t\tdelta = {res - t}')


def task1():
    a, b, n = 0, 1, 4
    x = np.linspace(a, b, n + 1)

    print('\nf(x) = x^3')
    f = lambda x: x ** 3
    show_res(1 / 4, simp(f, x), trap(f, x))

    print('\nf(x) = x^2')
    f = lambda x: x ** 2
    show_res(1 / 4, simp(f, x), trap(f, x))

    print('\nf(x) = x^3')
    f = lambda x: x / 2
    show_res(1 / 4, simp(f, x), trap(f, x))


def task2():
    # R = h^2 * M2 * (b - a) / 12
    # R < 10^-6
    # h < (10^-6 * 12/(M2 * (b - a))) ^ (1/2) = (10^-6 * 6) ^ (1/2)

    # f'' = 4*8 * x^2 * (x^2 + 1)^−3 − 2 * (x^2 + 1)^−2 < 8 * x^2 − 2
    # M2 < 24

    a, b, M2, eps = 0, 1, 24, 10 ** -6
    f = lambda x: 4/(1 + x ** 2)

    h = (eps * 12/(M2 * (b - a))) ** (1/2)
    x = np.linspace(a, b, int((b - a)/h + 1) + 1)

    t = trap(f, x)
    print(f'trapezoids method: \t{t}, \t\tdelta = {abs(math.pi - t)}')


def task3():
    a, b, eps = 0, 1, 10 ** -6
    f = lambda x: 4 / (1 + x ** 2)
    R = lambda Ih, Ih2: abs(Ih - Ih2) / 3

    h = (a - b)/2
    x1 = np.linspace(a, b, int((a - b) / h))
    x2 = np.linspace(a, b, int((a - b) / (h / 2)))

    while R(trap(f, x1), trap(f, x2)) >= eps:
        h /= 2
        x1 = np.linspace(a, b, int((a - b) / h))
        x2 = np.linspace(a, b, int((a - b) / (h / 2)))

    x = np.linspace(a, b, int((a - b) / (h / 2)))
    t = trap(f, x) * 4
    print(f'trapezoids method: \t{t}, \t\tdelta = {abs(math.pi - t)}')


def main():
    print('\n====== Task 1 ======')
    task1()

    print('\n====== Task 2 ======')
    task2()

    print('\n====== Task 3 ======')
    task3()


main()
