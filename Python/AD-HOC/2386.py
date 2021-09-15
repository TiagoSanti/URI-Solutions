A = int(input())
N = int(input())

cont = 0

for _ in range(N):
	F = int(input())

	F = F*A

	if F >= 40000000:
		cont += 1

print(cont)
