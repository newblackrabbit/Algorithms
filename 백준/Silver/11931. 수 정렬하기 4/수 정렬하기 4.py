import sys
input = sys.stdin.readline

n = int(input())
ans = []
for i in range(n):
    n = int(input())
    ans.append(n)

ans.sort(reverse=True)

for i in ans:
    print(i)
