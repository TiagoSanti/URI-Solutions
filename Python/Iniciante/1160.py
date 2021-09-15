T = int(input())

for i in range(T):
    PA, PB, G1, G2 = input().split(' ')
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)*0.01
    G2 = float(G2)*0.01

    year = 0
    while PA <= PB and year <= 100:
        PA += int(PA*G1)
        PB += int(PB*G2)
        year += 1

    if year > 100:
        print('Mais de 1 seculo.')
    else:
        print('{} anos.'.format(year))
