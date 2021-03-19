def sum(i, Gate, n, output_x, output_y):
    A = i
    B = n + i
    C = 2 * n + i
    print('GATE', Gate, 'AND', A, B)
    Gate += 1
    print('GATE', Gate, 'AND', A, C)
    Gate += 1
    print('GATE', Gate, 'AND', B, C)
    Gate += 1
    print('GATE', Gate, 'OR', Gate - 3, Gate - 2)
    Gate += 1
    print('GATE', Gate, 'OR', Gate - 2, Gate - 1)
    output_y.append(Gate)
    Gate += 1
    print('GATE', Gate, 'OR', A, B)
    Gate += 1
    print('GATE', Gate, 'OR', Gate - 1, C)
    Gate += 1
    print('GATE', Gate, 'AND', Gate - 7, C)
    Gate += 1
    print('GATE', Gate, 'NOT', output_y[i])
    Gate += 1
    print('GATE', Gate, 'AND', Gate - 1, Gate - 3)
    Gate += 1
    print('GATE', Gate, 'OR', Gate - 1, Gate - 3)
    output_x.append(Gate)
    Gate += 1
    return Gate, output_x, output_y
n = int(input())
Gate = 3 * n
output_x = []
output_y = []
output = 0
for i in range(n):
    Gate, output_x, output_y = sum(i, Gate, n, output_x, output_y)
print('GATE', Gate, 'AND', 3 * n + 4, 3 * n + 8)
output_x.append(Gate)
output_y.insert(0, Gate)
for i in range(len(output_x)):
    print('OUTPUT', output, output_x[i])
    output += 1
for i in range(len(output_y)):
    print('OUTPUT', output, output_y[i])
    output += 1
