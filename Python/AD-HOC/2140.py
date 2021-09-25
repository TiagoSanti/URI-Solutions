n, m = map(int, input().split())

while n != 0 and m != 0:

	troco = m - n
	notas = 0

	if troco > 1:
		while troco != 0 and notas <= 2:
			if troco >= 100:
				troco -= 100
				notas += 1
			elif troco >= 50:
				troco -= 50
				notas += 1
			elif troco >= 20:
				troco -= 20
				notas += 1
			elif troco >= 10:
				troco -= 10
				notas += 1
			elif troco >= 5:
				troco -= 5
				notas += 1
			elif troco >= 2:
				troco -= 2
				notas += 1

	if notas == 2:
		print('possible')
	else:
		print('impossible')

	n, m = map(int, input().split())
