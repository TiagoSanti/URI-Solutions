n = int(input())
mat = []
notas = []

for i in range(n):
    m, n = map(float, input().split())
    mat.append(m)
    notas.append(n)

if max(notas) < 8:
    print('Minimum note not reached')
else:
    print(int(mat[notas.index(max(notas))]))
