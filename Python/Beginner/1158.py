n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    sum = 0

    qnt = 1
    while qnt <= y:
        if x % 2 != 0:
            sum += x
            qnt += 1
        x += 1

    print(sum)
