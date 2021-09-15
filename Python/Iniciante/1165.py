N = int(input())

for i in range(N):
    X = int(input())

    is_prime = 1
    aux = 2
    while is_prime == 1 and aux < X:
        if X % aux == 0:
            is_prime = 0
        else:
            aux += 1

    if is_prime == 1:
        print('{} eh primo'.format(X))
    else:
        print('{} nao eh primo'.format(X))
