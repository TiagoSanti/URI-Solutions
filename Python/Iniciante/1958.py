X = input()

if float(X) < 0 or X[0] == '-':
    print('{:.4E}'.format(float(X)))
elif float(X) > 0 or X[0] != '-':
    print('+{:.4E}'.format(float(X)))
