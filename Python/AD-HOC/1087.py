x1, y1, x2, y2 = map(int, input().split())
while x1 != 0 and x2 != 0 and y1 != 0 and y2 != 0:

    distance = (abs(x2-x1), abs(y2-y1))

    moves = -1

    if distance[0] == 0 and distance[1] == 0:
        moves = 0
    elif distance[0] == distance[1] or distance[0] == 0 and distance[1] != 0 or distance[0] != 0 and distance[1] == 0:
        moves = 1
    else:
        moves = 2

    print(moves)

    x1, y1, x2, y2 = map(int, input().split())
