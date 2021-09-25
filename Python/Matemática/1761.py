from math import tan

while True:
	try:
		A, B, C = map(float, input().split())

		pi = 3.141592654
		conv = pi/180

		tamanho = (tan(A*conv) * B + C) * 5

		print('{:.2f}'.format(tamanho))

	except EOFError:
		break
		