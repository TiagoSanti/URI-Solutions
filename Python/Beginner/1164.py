N = int(input())

for i in range(N):
    X = int(input())

    sum = 1
    aux = 2

    if X != 1:
        while aux < X:
            if X % aux == 0:
                sum += aux

            aux += 1

        if sum == X:
            print('{} eh perfeito'.format(X))
        else:
            print('{} nao eh perfeito'.format(X))
    else:
        print('1 nao eh perfeito')
