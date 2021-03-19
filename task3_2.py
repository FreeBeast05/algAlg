import numpy as np

#таблица истинности
truth_table = np.zeros((16, 4), dtype=np.int32)

#вывод вершин
vertex_out = ''

#вывод значений вершин
value_out = ''

#индексы начала и конца формул длины 1,2,...
indexes = []

#множество для уже полученных таблиц истины
truth_table_set = set()

#значения переменных - входы
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11


#значения тождественных функций на входах
x1 = [0,0,1,1]
x2 = [0,1,0,1]


#добавляем сами переменные
truth_table[0] = x1
truth_table[1] = x2
size = 2

#добавляем отрицания переменных
for i in range(2):
    truth_table[size + i] = ~truth_table[i] + 2
    vertex_out += "GATE " + str(size + i) + ' NOT ' + str(i) + '\n'
    truth_table_set.add(tuple(truth_table[i]))
    truth_table_set.add(tuple(truth_table[size + i]))

size += 2
indexes.append((0, size))

#n - размер формул, количество переменных или их отрицаний
n = 2
while(size < 16):
    for t in range(1, int(n / 2) + 1):
        #соединяем формулы с длиннами t и n-t
        for i in range(indexes[t - 1][0], indexes[t - 1][1]):
            for j in range(indexes[n - t - 1][0], indexes[n - t - 1][1]):
                formula = truth_table[i] & truth_table[j]
                if tuple(formula) not in truth_table_set:
                    vertex_out += "GATE " + str(size) + ' AND ' + str(i) + ' ' + str(j) + '\n'

                    truth_table[size] = formula
                    truth_table_set.add(tuple(formula))
                    size += 1

                    # поддерживаем целостность:
                    # если уже получили формулу, то также имеем и её отрицание;
                    # если только получили формулу, то добавляем и её отрицание,
                    # но его в таблице еще быть не должно.
                    vertex_out += "GATE " + str(size) + ' NO ' + str(size - 1) + '\n'
                    truth_table[size] = ~formula + 2
                    truth_table_set.add(tuple(~formula + 2))
                    size += 1

    indexes.append((indexes[-1][1], size))
    n += 1

print(vertex_out[:-1])
print(value_out[:-1])