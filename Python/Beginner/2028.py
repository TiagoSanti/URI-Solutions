X = 1

while True:
	try:
		N = int(input())

		numeros = [0]
		for i in range(N+1):
			for j in range(i):
				numeros.append(i)

		if N == 0:
			print('Caso {}: 1 numero'.format(X))
		else:
			print('Caso {}: {} numeros'.format(X, len(numeros)))

		for i in range(len(numeros)):
			if i == len(numeros)-1:
				print('{}'.format(numeros[i]), end='')
			else:
				print('{} '.format(numeros[i]), end='')
		print('\n')

		X += 1

	except EOFError:
		break
