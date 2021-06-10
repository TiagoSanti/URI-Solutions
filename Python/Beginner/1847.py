A, B, C = map(int, input().split())

AB = abs(A - B)
BC = abs(B - C)

if B > A:
    if C < B:
        print(':(')
    else:
        if BC < AB:
            print(':(')
        else:
            print(':)')

elif B < A:
    if C > B:
        print(':)')
    else:
        if BC < AB:
            print(':)')
        else:
            print(':(')

else:
    if C > B:
        print(':)')
    else:
        print(':(')
