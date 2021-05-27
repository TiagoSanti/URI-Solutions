again = 0

while again != 2:
    x = float(input())

    while x < 0 or x > 10:
        print('nota invalida')

        x = float(input())

    y = float(input())

    while y < 0 or y > 10:
        print('nota invalida')

        y = float(input())

    print('media = {:.2f}'.format((x+y)/2))

    print('novo calculo (1-sim 2-nao)')
    again = int(input())
    while again != 1 and again != 2:
        print('novo calculo (1-sim 2-nao)')
        again = int(input())