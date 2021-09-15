N = int(input())

for _ in range(N):
	j1 = input()
	j2 = input()

	if j1 == j2:
		if j1 == 'papel':
			print('Ambos venceram')
		elif j1 == 'pedra':
			print('Sem ganhador')
		else:
			print('Aniquilacao mutua')
	else:
		if j1 == 'ataque' or j2 == 'papel' or j1 == 'pedra' and j2 == 'papel':
			print('Jogador 1 venceu')
		elif j2 == 'ataque' or j1 == 'papel' or j2 == 'pedra' and j1 == 'papel':
			print('Jogador 2 venceu')
