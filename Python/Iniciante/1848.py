for grito in range(3):
    num = 0
    inp = input()
    while inp != 'caw caw':
        inp = inp.replace('-', '0')
        inp = inp.replace('*', '1')
        num += int(inp, 2)

        inp = input()

    print(num)
