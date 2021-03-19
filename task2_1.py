n = int(input())
Gate =3*n
output=0
output_x=[]
output_y=[]
def sum(i,n, Gate, output_x, output_y):
    A=i
    B=n+i
    C=2*n+i
    print('GATE', Gate, 'OR', B ,C )
    Gate+=1
    print('GATE', Gate, 'AND', B, C)
    perenos_1=Gate
    Gate += 1
    print('GATE', Gate, 'NO', perenos_1 )
    Gate+=1
    print('GATE', Gate, 'AND', Gate-3, Gate-1)
    outpit_1=Gate
    Gate+=1
    print('GATE', Gate, 'OR', A ,outpit_1 )
    Gate += 1
    print('GATE', Gate, 'AND', A, outpit_1)
    perenos_2 = Gate
    Gate+=1
    print('GATE', Gate, 'NOT', Gate-1 )
    Gate+=1
    print('GATE', Gate, 'AND', Gate-3,Gate-1)
    output_y.append(Gate)
    Gate+=1
    print('GATE', Gate, 'OR', perenos_1 ,perenos_2)
    output_x.append(Gate)
    Gate+=1
    return Gate, output_x, output_y
for i in range(n):
    Gate, output_x, output_y =sum(i,n, Gate, output_x, output_y)
print('GATE', Gate, 'AND', 3*n+1, 3*n+2)
output_x.append(Gate)
output_y.insert(0, Gate)
for i in range(len(output_x)):
    print('OUTPUT', output, output_y[i])
    output+=1
for i in range(len(output_y)):
    print('OUTPUT', output, output_x[i])
    output += 1



