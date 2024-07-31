import sys
input = sys.stdin.readline

'''
돌 사람
1 상근
2 창영
3 상근
4 창영
5 상근
6 창영
홀 : 상근
짝 : 창영 
'''
n = int(input())

if n % 2 == 0:
    print('CY')
else:
    print('SK')
