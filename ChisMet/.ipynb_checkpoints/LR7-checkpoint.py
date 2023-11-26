import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp as eyler
from scipy.integrate import odeint
from math import cos, sin, exp, log


# Реализация метода Эйлера

def solve_eyler(f, X, h, y0):
    y = []
    y += [y0]

    for i in range(1, len(X)):
        y_i = y[i - 1] + h * f(X[i], y[i - 1])
        y += [y_i]

    return y


# Сравнение решений

def compare(sol1, sol2, x1, x2):
    plt.plot(x1, sol1, 'r--')
    plt.plot(x2, sol2)

    plt.grid()
    plt.show()


def task1():
    # Инициализация начальных значений

    a, b = 0, 5
    h = 1 / 16
    y0 = 1

    # Инициализация сетки

    X = np.linspace(a, b, int((b - a) / h + 1))

    # Инициализация функций

    f = lambda x, y: x ** 2     # дифф. уравнение

    # Инициальизация решений

    sol1 = solve_eyler(f, X, h, y0)                  # мое решение

    # Сравнение решений

    plt.plot(X, sol1, 'r')
    plt.grid()
    plt.show()


def task2():
    # Инициализация начальных значений

    a, b, N = 0, 15, 100
    y0 = (1, 0)

    # Инициализация сетки

    x1 = np.linspace(a, b, int(N / 2))      # Для точного решения
    x2 = np.linspace(a, b, N)               # Для решения солвера

    # Инициализация функций

    f = lambda y, x: [y[1], -2 * y[1] - 10 * y[0] + sin(x)]     # дифф. уравнение
    solution = lambda x: exp(-x) * (87 / 85 * cos(3 * x) + 26 / 85 * sin(3 * x)) \
                     + 1 / 85 * (9 * sin(x) - 2 * cos(x))       # точное решение

    # Инициальизация решений

    sol1 = [solution(x) for x in x1]    # мое решение
    sol2 = odeint(f, y0, x2)            # солвера

    # Сравнение решений

    plt.title('task2')
    compare(sol1, sol2[:, 0], x1, x2)

    # Красная линия точного решения
    # специально построена с меньшей точностью для наглядности


def task3():
    # Инициализация начальных значений

    a, b, N = 0.01, 15, 100
    t0 = 0.01
    y0 = [log(t0), 1/t0]

    # Инициализация сетки

    x1 = np.linspace(a, b, int(N / 2))      # Для точного решения
    x2 = np.linspace(a, b, N)               # Для решения солвера

    # Инициализация функций

    f = lambda y, x: [y[1], - 1 / x ** 2]   # дифф. уравнение
    solution = lambda x: log(x)             # точное решение

    # Инициальизация решений

    sol1 = [solution(x) for x in x1]    # мое решение
    sol2 = odeint(f, y0, x2)            # солвера

    # Сравнение решений

    plt.title('task3')
    compare(sol1, sol2[:, 0], x1, x2)

    # Красная линия точного решения
    # специально построена с меньшей точностью для наглядности


def main():
    task1()
    task2()
    task3()


main()