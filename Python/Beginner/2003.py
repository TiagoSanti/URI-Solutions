while 1:
	try:
		hora, minutos = map(int, input().split(':'))

		if hora <= 6:
			atraso = 0
		else:
			atraso = hora*60+minutos+60 - 480

		print('Atraso maximo:', atraso)

	except EOFError:
		break
