values = []
index = 1

for i in range(100):
    x = int(input())

    if i == 0:
        higher = x
    elif higher < x:
        higher = x
        index = i+1

print('{}\n{}'.format(higher, index))
