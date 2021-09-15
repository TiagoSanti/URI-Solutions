number = int(input())

sum = 0
qnt = 0

while number > 0:
    sum += number
    qnt += 1

    number = int(input())

avg = sum/qnt
print('{:.2f}'.format(avg))
