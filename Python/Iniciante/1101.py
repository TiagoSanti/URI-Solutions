m, n = map(int, input().split())

while m > 0 and n > 0:
    sum = 0

    if m > n:
        h = m
        l = n
    else:
        h = n
        l = m

    for i in range(l, h+1):
        sum += i
        print('{} '.format(i), end="")
    print('Sum={}'.format(sum))

    m, n = map(int, input().split())
