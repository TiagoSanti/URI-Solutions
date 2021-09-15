caso = 1

while True:
	try:
		N1 = input()
		N2 = input()

		qtd = 0

		k = 0
		while k <= len(N2) - len(N1):
			if N1[0] == N2[k]:
				sub = True
				pos = k
				j = 1
				l = k+1
				while sub and j < len(N1):
					if N1[j] != N2[l]:
						sub = False
					else:
						j += 1
						l += 1

				if sub == True:
					qtd += 1

			k += 1

		print('Caso #{}:'.format(caso))
		if qtd == 0:
			print('Nao existe subsequencia\n')
		else:
			print('Qtd.Subsequencias: {}'.format(qtd))
			print('Pos: {}\n'.format(pos+1))

		caso += 1

	except EOFError:
		break
