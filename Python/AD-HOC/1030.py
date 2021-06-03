NC = int(input())

for i in range(NC):
    n, k = map(int, input().split())

    posicao = 0

    for j in range(2, n+1, 1):
        posicao = (posicao + k) % j

    print("Case {}: {}".format(i+1, posicao+1))
