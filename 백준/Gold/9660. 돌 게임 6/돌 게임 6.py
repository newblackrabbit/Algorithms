('''
돌 이긴사람
1 상근
2 창영
3 상근
4 상근
5 창영
6 상근
7 창영
8 상근
9 창영 (4->3->1->1)
10 상근 (3->4->4)
11 상근 (4->4->3)
1 3 4 6 8 상근
2 5 7 9 창영 
''')   
import sys
input = sys.stdin.readline

n = int(input())

if n % 7 == 0 or n % 7 == 2:
    print('CY')
else:
    print('SK')
