import numpy as np
import math

def read_matrix():
    A = []
    first_str = []
    row = input().split()
    n = len(row)
    for i in range(n):
        first_str.append(int(row[i]))
    A.append(first_str)
    for i in range(n - 1):
        row = input().split()
        for i in range(len(row)):
            row[i] = int(row[i])
        A.append(row)
    return A


def check(A, n):
    if np.log2(n) % 2 == 0:
        A = np.array(A)
        return A
    else:
        for i in range(0, n):
            for j in range(n, 2 ** (math.ceil(np.log2(n)))):
                A[i] = np.append(A[i], 0)
        for i in range(n, 2 ** (math.ceil(np.log2(n)))):
            h = np.zeros((1, 2 ** (math.ceil(np.log2(n)))), dtype=int)
            A = np.concatenate((A, h))
        for i in range(n, 2 ** (math.ceil(np.log2(n)))):
            A[i][i] += 1
    return A


def splitting(A):
    global A11, A12, A21, A22
    A1, A2, A3, A4 = [], [], [], []
    l1 = len(A) // 2
    l2 = len(A[0]) // 2
    for str in A[:l1]:
        A1.append(str[:l2])
        A11 = np.array(A1)
    for str in A[:l1]:
        A2.append(str[l2:])
        A12 = np.array(A2)
    for str in A[l1:]:
        A3.append(str[:l2])
        A21 = np.array(A3)
    for str in A[l1:]:
        A4.append(str[l2:])
        A22 = np.array(A4)
    return A11, A12, A21, A22


def Shtrassen(A, B, n):
    if len(A) == 1:
        C = (A * B) % 9
        return C
    else:
        A11, A12, A21, A22 = splitting(A)
        B11, B12, B21, B22 = splitting(B)
        P1 = np.array(Shtrassen((A11 + A22), (B11 + B22), n / 2))
        P2 = np.array(Shtrassen((A21 + A22), B11, n / 2))
        P3 = np.array(Shtrassen(A11, (B12 - B22), n / 2))
        P4 = np.array(Shtrassen(A22, (B21 - B11), n / 2))
        P5 = np.array(Shtrassen((A11 + A12), B22, n / 2))
        P6 = np.array(Shtrassen((A21 - A11), (B11 + B12), n / 2))
        P7 = np.array(Shtrassen((A12 - A22), (B21 + B22), n / 2))
        C11 = ((P1 + P4 - P5 + P7)) % 9
        C12 = (P3 + P5) % 9
        C21 = (P2 + P4) % 9
        C22 = (P1 - P2 + P3 + P6) % 9
        k = len(C11) * 2
        C = [[0 for row in range(k)] for col in range(k)]
        for i in range(len(C11)):
            for j in range(len(C11)):
                C[i][j] = C11[i][j]
                C[i][j + len(C11)] = C12[i][j]
                C[i + len(C11)][j] = C21[i][j]
                C[i + len(C11)][j + len(C11)] = C22[i][j]
        return C


def Power(array, n, y):
    if y == 0:
        return np.eye(n)
    if (y % 2) == 1:
        return Shtrassen(Power(array, n, y - 1), array, n)
    else:
        array = Power(array, n, y / 2)
        return Shtrassen(array, array, n)


A = read_matrix()
n = len(A)
B = check(A, n)
ans = (Power(B, len(B), len(A)))
for i in range(n, len(B)):
    np.delete(ans, i, axis=0)
    np.delete(ans, i, axis=1)
for i in range(n):
    for j in range(n):
        print(int(ans[i][j]), end=' ')
    print()
