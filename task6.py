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
    A=np.array(A)
    return A, n
def LUP_decomposition(a, n, m):
    if n == 1:
        L = np.array([[1]])
        P = np.eye(m)
        if a[0,0]==0:
            for i in range(m):
                if a[0, i] == 1:
                    P[0, 0], P[i, i], P[i, 0], P[0, i] = 0, 0, 1, 1
                    break
        U = transposition(a, P)
        return L, U, P
    h1=math.ceil(n/2)
    h2=n-h1
    L1, U1, P1 = LUP_decomposition(a[0:h1], h1, m)
    D = transposition(a[h1:], np.transpose(P1))
    F=D[:,0:h1]
    E=converse(U1[:,0:h1])
    FE = Shtrassen(F,E)
    G =(D-Shtrassen(FE, U1))%2
    L2, U2, P2 = LUP_decomposition(G[:,h1:], h2, m - h1)
    p3 = np.zeros((m, m))
    for i in range(h1):
        p3[i, i] = 1
    for i in range(h1, m):
        for j in range(h1, m):
            p3[i, j] = P2[i - h1, j - h1]
    H = transposition(U1, np.transpose(p3))
    L = np.zeros((n, n))
    for i in range(h1):
        for j in range(i + 1):
            L[i, j] = L1[i, j]
    for i in range(h2):
        for j in range(h1):
            L[h1 + i, j] = FE[i, j]
    for i in range(h2):
        for j in range(i + 1):
            L[h1 + i, h1 + j] = L2[i, j]
    U = np.zeros((n, m))
    for i in range(h1):
        for j in range(i, m):
            U[i, j] = H[i, j]
    for i in range(h2):
        for j in range(i, m - h1):
            U[h1 + i, h1 + j] = U2[i, j]
    P = transposition(p3, P1)
    return L, U, P

def transposition(A, P):
    result=np.zeros((len(A), len(A[0])))
    indexes=[]
    for i in range(len(A[0])):
        for j in range(len(A[0])):
            if P[i][j]==1:
                indexes.append(j)
    for i in range(len(A[0])):
        for j in range(len(A)):
            ind=indexes[i]
            result[j,ind]=A[j, i]
    return result

def converse(a):
    n = len(a[0])
    if n!=1:
        half_size = n // 2
        b=a[0:half_size,half_size:]
        c=converse(a[half_size:,half_size:])
        a=converse(a[0:half_size,0:half_size])
        prom=Shtrassen(a,b)
        b = Shtrassen(prom, c)
        result = np.zeros((n, n))
        result[0:half_size, 0:half_size] = np.copy(a)
        result[0:half_size, half_size:] = np.copy(b)
        result[half_size:, half_size:] = np.copy(c)
        return result
    elif n == 1:
        return a


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
def Shtrassen(A, B):
    n=len(A)
    r=len(A[0])
    m=len(B)
    l=len(B[0])
    step = 1
    while step < max(n, m, l):
        step *= 2
    prom = np.zeros((step, step))
    prom[0:n, 0:r] = A
    A = np.copy(prom)
    prom_B = np.zeros((step, step))
    prom_B[:m, :l] = B
    B = np.copy(prom_B)
    if len(A) == 1:
        C = (A * B) % 2
        return C
    else:
        A11, A12, A21, A22 = splitting(A)
        B11, B12, B21, B22 = splitting(B)
        P1 = np.array(Shtrassen((A11 + A22), (B11 + B22) ))
        P2 = np.array(Shtrassen((A21 + A22), B11))
        P3 = np.array(Shtrassen(A11, (B12 - B22)))
        P4 = np.array(Shtrassen(A22, (B21 - B11)))
        P5 = np.array(Shtrassen((A11 + A12), B22))
        P6 = np.array(Shtrassen((A21 - A11), (B11 + B12)))
        P7 = np.array(Shtrassen((A12 - A22), (B21 + B22)))
        C11 = ((P1 + P4 - P5 + P7)) % 2
        C12 = (P3 + P5) % 2
        C21 = (P2 + P4) % 2
        C22 = (P1 - P2 + P3 + P6) % 2
        k = len(C11) * 2
        C = [[0 for row in range(k)] for col in range(k)]
        for i in range(len(C11)):
            for j in range(len(C11)):
                C[i][j] = C11[i][j]
                C[i][j + len(C11)] = C12[i][j]
                C[i + len(C11)][j] = C21[i][j]
                C[i + len(C11)][j + len(C11)] = C22[i][j]
        C=np.array(C)
        C=C[:n,0:l]
        return C

A, n=read_matrix()
L, U, P = LUP_decomposition(A,n,n)
for i in range(len(L)):
    for j in range(len(U[0])):
        k=L[i][j]
        print(int(k), end=' ')
    print()
for i in range(len(U)):
    for j in range(len(U[0])):
        k = U[i][j]
        print(int(k), end=' ')
    print()
for i in range(len(P)):
    for j in range(len(P[0])):
        k = P[i][j]
        print(int(k), end=' ')
    print()
