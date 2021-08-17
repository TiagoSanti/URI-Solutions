pi = 3.14

while True:
	try:
		volume = float(input())
		diametro = float(input())

		raio = diametro/2

		area = pi * (diametro/2)**2

		altura = volume/area

		print('ALTURA = {:.2f}\n'
		      'AREA = {:.2f}'.format(altura, area))

	except EOFError:
		break
