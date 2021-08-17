N, M = map(int, input().split())

terreno = []

X, Y = 0, 0

for i in range(N):
	terreno.append(list(map(int, input().split())))

for i in range(1, N-1):
	for j in range(1, M-1):
		if terreno[i][j] == 42:
			if terreno[i-1][j-1] == 7 and terreno[i-1][j] == 7 and terreno[i-1][j+1] == 7:
				if terreno[i][j-1] == 7 and terreno[i][j+1] == 7:
					if terreno[i+1][j-1] == 7 and terreno[i+1][j] == 7 and terreno[i+1][j+1] == 7:
						X, Y = i+1, j+1

print(X, Y)
