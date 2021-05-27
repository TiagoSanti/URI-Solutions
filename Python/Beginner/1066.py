even = 0
odd = 0
pos = 0
neg = 0

for i in range(5):
    num = int(input())

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1

print(f'{even} valor(es) par(es)\n{odd} valor(es) impar(es)\n{pos} valor(es) positivo(s)\n{neg} valor(es) negativo(s)')
