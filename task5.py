import numpy as np


def determinant(matrix, n):
    for i in range(n):
        maximum = abs(matrix[i][i])
        str = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > maximum:
                maximum = abs(matrix[j][i])
                str = j
        if abs(maximum) <= 0.0001:
            return print('no')
        if i != str:
            matrix[i], matrix[str] = np.copy(matrix[str]), np.copy(matrix[i])
        for j in range(i + 1, n):
            k = matrix[j][i] / matrix[i][i]
            matrix[j] -= matrix[i] * k
    return print('yes')


input_arc = []
n = int(input())
for i in range(n):
    vertex1, vertex2 = [int(i) for i in input().split(' ')]
    input_arc.append((vertex1, vertex2))
size = max(input_arc[n - 1]) + 1
adjacency_matrix = np.zeros((size, size))
for vertex1, vertex2 in input_arc:
    adjacency_matrix[vertex1][vertex2] = np.random.randint(1, 10)
determinant(adjacency_matrix, size)
