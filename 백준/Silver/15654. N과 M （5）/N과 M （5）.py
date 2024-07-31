import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
lst = []

def backtracking():
    if len(lst) == m:
        print(' '.join(map(str,lst)))
        return
    
    for i in num:
        if i not in lst:
            lst.append(i)
            backtracking()
            lst.pop()
            
backtracking()
