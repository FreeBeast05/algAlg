import numpy as np

n = int(input())
resides = []
for i in range(n):
    if i ** 2 % (n - 1) != 0:
        resides.append(i ** 2 % (n - 1))
legandre = {}
for i in range(-n + 2, n - 1):
    if (n + i - 1) % (n - 1) in resides:
        legandre[i] = 1
    elif i == 0:
        continue
    else:
        legandre[i] = -1
adamar_array = np.zeros((n, n), dtype=int)
adamar_array[:, 0] = 1
adamar_array[0, :] = 1
for i in range(1, n):
    for j in range(1, n):
        if i == j:
            adamar_array[i, j] = 0
        else:
            if legandre[i - j] == -1:
                adamar_array[i, j] = 0
            else:
                adamar_array[i, j] = 1

for string in adamar_array:
    for i in string:
        print(i, end="")
    print()
    for j in string:
        if j == 1:
            print(0, end='')
        else:
            print(1, end='')
    print()
