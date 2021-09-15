T = int(input())

respostas = list(map(int, input().split()))

num = 0
for i in respostas:
	if i == T:
		num += 1

print(num)
