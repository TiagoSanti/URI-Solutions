S, T, F = map(int, input().split())

hora = S + T + F

if hora == 24:
	hora = 0
elif hora > 24:
	hora -= 24
elif hora < 0:
	hora += 24

print(hora)
