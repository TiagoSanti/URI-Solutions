x = int(input())

if x % 2 == 0:
    odd = x + 1
else:
    odd = x

for i in range(6):
    print(odd)
    odd = odd + 2
