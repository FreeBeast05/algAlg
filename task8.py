import numpy as np
from numpy import linalg

edges = int(input())
vertexs = {}
count = 0
contiguity = {}
for i in range(edges):
    string = input()
    vert_1, vert_2 = string.split(' ')
    if vert_1 not in vertexs:
        vertexs[vert_1] = count
        count += 1
    if vert_2 not in vertexs:
        vertexs[vert_2] = count
        count += 1
    vert_1, vert_2 = vertexs[vert_1], vertexs[vert_2]
    if vert_1 not in contiguity:
        contiguity[vert_1] = []
    if vert_2 not in contiguity:
        contiguity[vert_2] = []
    contiguity[vert_1].append(vert_2)
    contiguity[vert_2].append(vert_1)
contiguity = {k: list(set(j)) for k, j in contiguity.items()}
size = sorted(contiguity)[-1] + 1
Laplas_matrix = np.zeros((size, size))
for i in contiguity.keys():
    for j in contiguity[i]:
            Laplas_matrix[i,i]=len(contiguity[i])
            Laplas_matrix[i,j]=-1
w, v = linalg.eigh(Laplas_matrix)
vector_2 = v[:, 1]
reserval = []
vector_includ = {}
for i in range(len(vector_2)):
    vector_includ[vector_2[i]] = i
vector_includ = sorted(vector_includ.items(), key=lambda k: k[0], reverse=True)
for i in vector_includ:
    reserval.append(i[1])
density = []
for j in range(1, size):
    subvector = reserval[:j]
    counter = 0
    for vert_1 in subvector:
        for vert_2 in contiguity[vert_1]:
            if vert_2 not in subvector:
                counter += 1
    density.append(size * counter / (j * (size - j)))
density = np.array(density)
indexs = np.where(density == density.min())[0]
output = []
for index in indexs:
    index += 1
    if index < size //2:
        slice = reserval[:index]
    else:
        slice = reserval[index:]
    output_vertices = []
    for key, value in vertexs.items():
        if value in slice:
            output.append(int(key))
print(min(output))
