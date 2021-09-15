i = 1
j = 7

for k in range(5):
    for l in range(3):
        print('I={} J={}'.format(i, j))
        j -= 1
    j += 5
    i += 2
