'''
돌 이긴사람
1 상근
2 창영
3 상근
4 상근
5 창영
6 상근
7 창영
8 상근 
9 상근
10 창영

5로 나눴을 때 나머지 0,2면 창영 승
'''
n = int(input())

if n % 5 == 0 or n % 5 == 2:
    print('CY')
else:
    print('SK')
