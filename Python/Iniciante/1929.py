A, B, C, D = map(int, input().split())

possivel = 'N'

if abs(B-C) < A < B+C or abs(B+D) < A < B+D or abs(C+D) < A < C+D:
    possivel = 'S'

if abs(A-C) < B < A+C or abs(A-D) < B < A+D or abs(C-D) < B < C+D:
    possivel = 'S'

if abs(A-B) < C < A+B or abs(A-D) < C < A+D or abs(B-D) < C < B-D:
    possivel = 'S'

if abs(A-B) < D < A+B or abs(A-C) < D < A+C or abs(B-C) < D < B+C:
    possivel = 'S'

print(possivel)
