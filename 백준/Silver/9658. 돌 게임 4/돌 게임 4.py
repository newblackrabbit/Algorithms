'''
돌 이긴사람
1 창영
2 상근
3 창영
4 상근
5 상근
6 상근
7 상근
8 창영
9 상근
10 창영

...

'''

n = int(input())

if n % 7 == 1 or n % 7 == 3:
    print('CY')
else:
    print('SK')
