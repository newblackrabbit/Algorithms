import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    m = int(input())
    lst = list(map(int,input().split()))
    print(sum(lst))
