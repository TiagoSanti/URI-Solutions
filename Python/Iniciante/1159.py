X = int(input())

while X != 0:
    sum = 0

    if X % 2 != 0:
        X += 1

    for i in range(5):
        sum += X
        X += 2

    print(sum)

    X = int(input())
