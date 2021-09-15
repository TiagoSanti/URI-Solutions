def sum(n1, d1, n2, d2):
	r1 = n1*d2 + n2*d1
	r2 = d1*d2

	return r1, r2


def sub(n1, d1, n2, d2):
	r1 = n1*d2 - n2*d1
	r2 = d1*d2

	return r1, r2


def mult(n1, d1, n2, d2):
	r1 = n1*n2
	r2 = d1*d2

	return r1, r2


def div(n1, d1, n2, d2):
	r1 = n1*d2
	r2 = n2*d1

	return r1, r2


def simpl(r1, r2):
	i = 2
	s1 = r1
	s2 = r2

	while i <= min(abs(s1), abs(s2)):
		if s1 % i == 0 and s2 % i == 0:
			s1 /= i
			s2 /= i

			i = 2
		else:
			i += 1

	return s1, s2


n = int(input())
for _ in range(n):
	n1, _, d1, op, n2, _, d2 = input().split()

	n1 = int(n1)
	d1 = int(d1)
	n2 = int(n2)
	d2 = int(d2)

	if op == '+':
		r1, r2 = sum(n1, d1, n2, d2)

	elif op == '-':
		r1, r2 = sub(n1, d1, n2, d2)

	elif op == '*':
		r1, r2 = mult(n1, d1, n2, d2)

	elif op == '/':
		r1, r2 = div(n1, d1, n2, d2)

	s1, s2 = map(int, simpl(r1, r2))

	print(f'{r1}/{r2} = {s1}/{s2}')
