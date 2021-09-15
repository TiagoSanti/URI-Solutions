QT = int(input())

for i in range(QT):
    j1, e1, j2, e2 = input().split()
    N, M = map(int, input().split())

    if (N+M) % 2 == 0:
        if e1 == 'PAR':
            print(j1)
        else:
            print(j2)
    else:
        if e1 == 'IMPAR':
            print(j1)
        else:
            print(j2)
