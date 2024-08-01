import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int,input().split()))
# 3 1 6 2 7 30 1
lst.sort()
# 1 1 2 3 6 7 30
num = 1
for i in lst:
    if num  < i:
        break

    num += i

print(num)
    
        
