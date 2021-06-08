A, D = map(int, input().split())

while A != 0 and D != 0:
    atacantes = list(map(int, input().split()))
    defensores = list(map(int, input().split()))

    defensores.pop(defensores.index(min(defensores)))
    penultimoD = min(defensores)

    ultimoA = min(atacantes)
    if ultimoA < penultimoD:
        print('Y')
    else:
        print('N')

    A, D = map(int, input().split())
