x = int(input())
z = int(input())

while z <= x:
    z = int(input())

sum = x
qtd = 1

while sum <= z:
    sum += (x+qtd)
    qtd += 1

print(qtd)