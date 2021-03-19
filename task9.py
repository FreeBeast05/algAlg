import random

numbers = int(input())
weights = []
for i in range(numbers):
    weights.append(int(input()))
edges_numbers = int(input())
edges = {}
for i in range(edges_numbers):
    edges[i] = []
    for k in input().split(' '):
        edges[i].append(int(k))
mix_edges = sorted(edges.keys(), key=lambda A: random.random())
for i in mix_edges:
    vertex_1 = edges[i][0]
    vertex_2 = edges[i][1]
    if weights[vertex_1] * weights[vertex_2] != 0:
        minimum = min(weights[vertex_1], weights[vertex_2])
        weights[vertex_1] -= minimum
        weights[vertex_2] -= minimum
output = []
for i, k in enumerate(weights):
    if k == 0:
        output.append(str(i))
print(' '.join(output))
