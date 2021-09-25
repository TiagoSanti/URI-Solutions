while True:
	try:
		n = int(input())

		arvore = []

		j = 0
		for i in range(n, 0, -2):
			arvore.insert(0, j*' ' + '*'*i)
			j += 1
		arvore.append(int(len(arvore[-1])/2)*' ' + '*')
		arvore.append(((int(len(arvore[-2])/2))-1)*' ' + '*'*3)

		for i in arvore:
			print(i)
		print()

	except EOFError:
		break
