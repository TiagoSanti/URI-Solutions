produtos = {
	1001: 1.5,
	1002: 2.5,
	1003: 3.5,
	1004: 4.5,
	1005: 5.5
}

p = int(input())

total = 0
for _ in range(p):
	prod, q = map(int, input().split())

	total += produtos[prod] * q

print('{:.2f}'.format(total))
