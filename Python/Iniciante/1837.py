a, b = map(int, input().split())

r = a % abs(b)
q = (a - r)//b
print('{} {}'.format(q, r))

# a = b*q + r
# q = (a - r)/b
