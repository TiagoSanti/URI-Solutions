import numpy as np

line = int(input())
operation = input()

matrix = np.zeros((3, 3))
total = 0

for i in range(3):
    for j in range(3):
        matrix[i][j] = int(input())

for i in range(3):
    for j in range(3):
        print('{} '.format(matrix[i][j]))
    print()

for j in range(3):
    if operation == 'S':
        total += matrix[line][j]
    elif operation == 'M':
        total *= matrix[line][j]

print('{:.1f}'.format(total))
