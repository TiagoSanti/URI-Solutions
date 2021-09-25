def join(array):
	index = 0

	i = index+1
	while i < len(array):
		if array[i][2] == array[index][2]:
			array[index][0] += array[i][0]
			array[index][1] += array[i][1]
			array.pop(i)

			i = index+1

		else:
			index += 1
			i += 1

	return array


cidade = 1

imoveis = int(input())
while imoveis != 0:
	pares = []
	total_m = 0
	total_c = 0

	for i in range(imoveis):
		qtd_moradores, consumo_total = map(int, input().split())

		total_m += qtd_moradores
		total_c += consumo_total

		pares.append([qtd_moradores, consumo_total, int(consumo_total/qtd_moradores)])

	pares.sort(key=lambda array: array[2])
	# def funcao(array): return array[2]
	pares = join(pares)

	if cidade == 1:
		print(f'Cidade# 1:')
	else:
		print(f'\nCidade# {cidade}:')

	for i in range(len(pares)):
		if i != len(pares)-1:
			print(f'{pares[i][0]}-{pares[i][2]} ', end='')
		else:
			print(f'{pares[i][0]}-{pares[i][2]}')

	consumo_medio = total_c/total_m
	if consumo_medio % 0.01 > 0.0099:
		print('Consumo medio: {:.2f} m3.'.format(consumo_medio))
	else:
		print('Consumo medio: {:.2f} m3.'.format(consumo_medio - consumo_medio % 0.01)) # formato para não arredondar

	imoveis = int(input())
	cidade += 1
