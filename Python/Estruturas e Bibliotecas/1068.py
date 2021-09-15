while True:
	try:
		pilha = input()

		correct = 1
		par = 0
		i = 0
		while i < len(pilha) and correct:
			if pilha[i] == '(':
				par += 1
				#print('1', i, par)

			if pilha[i] == ')':
				if par == 0:
					correct = 0
					#print('2', i, par)
				else:
					par -= 1
					#print('3', i, par)

			if i == len(pilha)-1:
				if par % 2 != 0:
					correct = 0
					#print('5', i, par)

			i += 1

		if correct:
			print('correct')
		else:
			print('incorrect')

	except EOFError:
		break
