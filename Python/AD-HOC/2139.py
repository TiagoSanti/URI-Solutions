while True:
	try:
		mes, dia = map(int, input().split())

		meses = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30}

		dias = 0

		if mes == 12:
			if dia == 25:
				print('E natal!')
			elif dia == 24:
				print('E vespera de natal!')
			elif dia > 25:
				print('Ja passou!')
			else:
				print(f'Faltam {25 - dia} dias para o natal!')
		else:
			for i in range(11, mes - 1, -1):
				if i != mes:
					dias += meses[i]
				else:
					dias += meses[i] - dia

			dias += 25

			print(f'Faltam {dias} dias para o natal!')
	except EOFError:
		break