a, b, c = map(int, input().split())

possivel = 0

if a-b == 0 or a-c == 0 or b-c == 0:
	possivel = 1

if max(a, b, c) == a:
	if a-b-c == 0:
		possivel = 1
elif max(a, b, c) == b:
	if b-a-c == 0:
		possivel = 1
elif max(a, b, c) == c:
	if c-a-b == 0:
		possivel = 1

if possivel:
	print('S')
else:
	print('N')
