x = float(input())

while x < 0 or x > 10:
    print('nota invalida')

    x = float(input())

y = float(input())

while y < 0 or y > 10:
    print('nota invalida')

    y = float(input())

print('media = {:.2f}'.format((x+y)/2))