while True:
    try:
        L = int(input())
        V = list(map(int, input().split()))

        if max(V) < 10:
            print('1')
        elif 10 <= max(V) < 20:
            print('2')
        else:
            print('3')

    except EOFError:
        break
