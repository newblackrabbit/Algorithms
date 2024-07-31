import sys
input = sys.stdin.readline

n,m = map(int,input().split())

lst = []

def backtracking(k):
    if len(lst) == m:
        print(' '.join(map(str,lst)))
        return
    
    for i in range(k,n+1):
        #if i not in lst:
        lst.append(i)
        backtracking(i)
        lst.pop()
            
backtracking(1)
