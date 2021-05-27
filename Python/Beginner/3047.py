M = int(input())
if 40 <= M <= 110:
    A = int(input())
    if 1 <= A < M:
        B = int(input())
        if 1 <= B < M and A != B:
            C = M - A - B
            print(max(A, B, C))
