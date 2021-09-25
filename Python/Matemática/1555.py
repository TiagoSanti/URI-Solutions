r = lambda x, y: (3*x)**2 + y**2
b = lambda x, y: 2*(x**2) + (5*y)**2
c = lambda x, y: -100*x + y**3

n = int(input())

for _ in range(n):
	x, y = map(int, input().split())

	rafael = r(x, y)
	beto = b(x, y)
	carlos = c(x, y)

	if rafael > beto and rafael > carlos:
		print('Rafael ganhou')
	elif beto > rafael and beto > carlos:
		print('Beto ganhou')
	else:
		print('Carlos ganhou')
