def primo(x):
	raiz = int(x**0.5)

	if x != 2 and x % 2 == 0 or x == 1:
		return False

	i = 3
	while i <= raiz:
		if x % i == 0:
			return False

		i += 2

	return True


while True:
	try:
		m = int(input())

		moedas = []
		valor = 0

		for _ in range(m):
			moedas.append(int(input()))

		n = int(input())

		i = m-1
		while i >= 0:
			valor += moedas[i]
			i -= n

		if primo(valor):
			print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
		else:
			print('Bad boy! I’ll hit you.')

	except EOFError:
		break
