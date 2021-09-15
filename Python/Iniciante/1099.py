n = int(input())

for i in range(n):
    sum = 0

    x, y = map(int, input().split())

    if x > y:
        beg = y
        end = x
    else:
        beg = x
        end = y

    if beg % 2 == 0:
        aux = beg+1
    else:
        aux = beg+2

    while aux < end:
        sum += aux
        aux += 2

    print(sum)
