# TODO Fix -> Time limit exceeded

N = int(input())

pes = []
maior_distancia = 0
pi = 3.14

for _ in range(N):
	coord = list(map(float, input().split()))
	print(coord)
	pes.append(coord)

for i in range(N):
	for j in range(i+1, N):
		distancia = ((pes[i][0]-pes[j][0])**2 + (pes[i][1]-pes[j][1])**2)**0.5

		if distancia > maior_distancia:
			maior_distancia = distancia
			p1 = pes[i]
			p2 = pes[j]

raio = maior_distancia/2
metragem = 2*pi*raio * 4
x = (p1[0]+p2[0])/2
y = (p1[1]+p2[1])/2

print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(x, y, raio, metragem))
