import math

import matplotlib.pyplot as plt
import sympy as sy
import numpy as np


def get_diff(f):
    return lambda x, h: (f(x + h) - f(x - h)) / (2 * h)


f = lambda x: math.cosh(x / 4)
eps = 1.1
M_2 = 1 / 16 * math.cosh(2 * eps / 4)
df = 1 / 4 * math.sinh(eps / 4)
f_h = lambda x, h: (f(x + h) - f(x)) / h
f_2h = get_diff(f)


print('Задание 1')

delta = 10 ** -3

h_opt = delta * 2 / M_2
print(f"eps = 10^-3\n"
      f"f`(eps) ~= {f_2h(eps, h_opt)}\n"
      f"f`(eps)  = {df}")

delta = 10 ** -6

h_opt = delta * 2 / M_2
print(f"eps = 10^-6\n"
      f"f`(eps) ~= {f_2h(eps, h_opt)}\n"
      f"f`(eps)  = {df}")


h = [1 / 2, 1 / 4, 1 / 8]
print('Задание 2')
print(f"f_h  = {df - f_h(eps, h[0]), df - f_h(eps, h[1]), df - f_h(eps, h[2])}")
print(f"f_2h = {df - f_2h(eps, h[0]), df - f_2h(eps, h[1]), df - f_2h(eps, h[2])}")
# print(f"th_2h = {th_2h(h[0]), th_2h(h[1]), th_2h(h[2])}")


print('Задание 3')
x = np.array([i for i in range(30)])
e = np.array([abs(df - f_h(eps, 1/2**i)) for i in x])
delta = [M_2 * 1/2**i / 2 for i in range(1, 31)]

print(delta)
print(e)

p1 = plt.plot(x, e)
plt.grid()
plt.show()

