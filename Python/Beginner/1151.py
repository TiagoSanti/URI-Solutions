n = int(input())

last = 1
lastlast = 0

print('0 1 ', end="")
for i in range(n-2):
    now = last+lastlast
    if i == n-3:
        print('{}'.format(now))
    else:
        print('{} '.format(now), end="")

    lastlast = last
    last = now