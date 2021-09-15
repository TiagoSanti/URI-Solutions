while True:
	try:
		Xf, Yf, Xi, Yi, Vi, R1, R2 = map(int, input().split())

		distancia = ((Xi - Xf)**2 + (Yi - Yf)**2)**0.5 + Vi*1.5 - R1

		if distancia <= R2:
			print('Y')
		else:
			print('N')

	except EOFError:
		break
