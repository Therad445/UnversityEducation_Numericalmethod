import numpy as np
import random as rd
import sympy as sp


def solve_inv(A, B):
    if np.linalg.det(A):
        return np.dot(np.linalg.inv(A), B)


def solve_kramer(A, B):
    if not np.linalg.det(A):
        return None

    X = []
    dA = np.linalg.det(A)
    for i in range(0, A.shape[1]):
        buf = np.copy(A)
        buf[:, i][:, np.newaxis] = B
        X += [np.linalg.det(buf)/dA]

    return X


def diag(A, B):
    n = A.shape[0]

    A = np.array(A)
    B = np.array(B)

    for i in range(n):
        col = list(map(abs, A[:, i]))[i:n]
        row_A = np.array(A[i, :])
        row_B = np.array(B[i, 0])

        main_index = col.index(max(col)) + i
        main_el = A[main_index, i]

        A[i, :], A[main_index, :] = A[main_index, :], row_A
        B[i, 0], B[main_index, 0] = B[main_index, 0], row_B

        for j in range(i, n):
            A[i, j] /= main_el
        B[i, 0] /= main_el

        row = np.array(A[i, :])

        for j in range(i + 1, n):
            k = A[j, i]
            A[j, :] -= row*k
            B[j, 0] -= B[i, 0]*k

    return A, B


def solve_gauss(A, B):
    n = A.shape[1]

    X = np.zeros((n, 1))

    X[n - 1, 0] = B[n - 1, 0]

    for i in range(n - 2, -1, -1):
        c = 0
        for j in range(n - 1, i, -1):
            c += A[i, j] * X[j, 0]

        X[i, 0] = B[i, 0] - c

    return X


def solve_rref(A, B):
    n = A.shape[0]

    A = np.array(A).T
    B = np.array(B).T
    Q = np.vstack((A, B)).T

    Q = sp.Matrix(Q).rref()[0]

    return np.array(sp.Matrix(Q[:, n]))


def task1():
    n = 5
    cond = 10**3

    A = np.random.random((n, n))

    while np.linalg.cond(A) < cond:
        A = np.random.random((n, n))

    B = np.random.random((n, 1))

    print(solve_inv(A, B))
    print(solve_kramer(A, B))
    print(solve_gauss(*diag(A, B)))
    print(solve_rref(A, B))


task1()
