sum = 1
num = 3
den = 2

for i in range(19):
    sum += float(num/den)

    num += 2
    den *= 2

print('{:.2f}'.format(sum))
