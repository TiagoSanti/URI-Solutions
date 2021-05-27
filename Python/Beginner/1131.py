again = 1
inter_v = 0
gremio_v = 0
draw = 0

while again == 1:
    inter_g, gremio_g = map(int, input().split())

    if gremio_g == inter_g:
        draw += 1
    elif gremio_g > inter_g:
        gremio_v += 1
    elif inter_g > gremio_g:
        inter_v += 1

    print('Novo grenal (1-sim 2-nao)')
    again = int(input())

print('{} grenais\n'
      'Inter:{}\n'
      'Gremio:{}\n'
      'Empates:{}'.format(gremio_v+inter_v+draw, inter_v, gremio_v, draw))

if gremio_v > inter_v:
    print('Gremio venceu mais')
elif inter_v > gremio_v:
    print('Inter venceu mais')
else:
    print('Nao houve vencedor')
