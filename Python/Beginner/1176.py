def Fib(fib, i, j):
	for k in range(i, j):
		fib.append(fib[k-1] + fib[k-2])

	return fib


fib = [0, 1]
i = 1

t = int(input())

for _ in range(t):
	n = int(input())

	if n > i:
		Fib(fib, i+1, n+1)
		i = n

	print(f'Fib({n}) = {fib[n]}')
