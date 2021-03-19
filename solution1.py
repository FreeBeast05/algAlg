import numpy as np
import math

n = int(input())
start_pozition = [0]
number_gate = n
count = 0
stop = False
vihod = 1
for stepen in range(0, math.ceil(np.log2(n) + 1)):
    if stepen == 0:
        second_gate = number_gate - n + 1
    else:
        second_gate = number_gate - n + 2 ** stepen
    for i in range(2 ** stepen):
        print("GATE", number_gate, 'OR', start_pozition[i], second_gate)
        start_pozition.append(number_gate)
        second_gate += 1
        number_gate += 1
        last = start_pozition[i] + 1
        count += 1
        if stepen == math.ceil(np.log2(n) - 1) and count == n - 1:
            stop = True
            break
    if (stop):
        break
    if stepen == 0:
        second_gate = number_gate - n + 1
    else:
        second_gate = number_gate - n + 2 ** stepen
    for j in range(n - 2 ** (stepen + 1)):
        print("GATE", number_gate, 'OR', last, second_gate)
        last += 1
        second_gate += 1
        number_gate += 1
print('OUTPUT', 0, 0)
number_gate = n
for v in range(math.ceil(np.log2(n))):
    for i in range(2 ** v):
        if vihod == n:
            break
        print('OUTPUT', vihod, number_gate)
        number_gate += 1
        vihod += 1
    number_gate += n - (2 ** v) * 2
