input = input().split()

A = int(input[0])
N = int(input[-1])

sum = 0

for i in range(0, N):
    sum += A+i

print(sum)
