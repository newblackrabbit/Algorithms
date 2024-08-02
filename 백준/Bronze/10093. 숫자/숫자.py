a,b = map(int,input().split())
n = min(a,b)
m = max(a,b)
if m-n <= 1:
    print(0)
else:
    print(m-n-1)
for i in range(n+1,m):
    print(i,end=' ')
