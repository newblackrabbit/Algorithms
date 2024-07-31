import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
lst = []

def backtracking(start):
    if len(lst) == m:
        print(' '.join(map(str,lst)))
        return
    
    for i in range(start,n):
        if num[i] not in lst:
            lst.append(num[i])
            backtracking(i+1)
            lst.pop()
            
backtracking(0)
