import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = []

def backtracking(k):
    if len(lst) == m:
        print(' '.join(map(str,lst)))

    for i in range(k,n+1):
        if i not in lst:
            lst.append(i)
            backtracking(i+1)
            lst.pop()
            
backtracking(1)
