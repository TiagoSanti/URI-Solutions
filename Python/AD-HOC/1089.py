while True:
    N = int(input())

    if N == 0:
        break
    else:
        mag = list(map(int, input().split()))
        mag.append(mag[0])

        p = 0
        for i in range(N):

            if i == 0:
                back = mag[i-2]
            else:
                back = mag[i-1]
            next = mag[i + 1]
            this = mag[i]

            if back < this > next or back > this < next:
                p += 1

        print(p)