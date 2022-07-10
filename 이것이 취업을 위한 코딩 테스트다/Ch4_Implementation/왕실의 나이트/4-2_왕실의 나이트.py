'''
해결 방법 -
1. 나이트의 이동 방향을 알아내어, 현재 나이트의 위치에 더할 것.
'''

place = input()

alphabet = list('abcdefgh')
map_size = 8
c = 0

x = alphabet.index(place[0])
y = int(place[1])
