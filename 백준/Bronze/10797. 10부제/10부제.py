n = int(input())
m = list(map(int,input().split()))
count = 0

for i in range(len(m)):
    if n == m[i]:
        count += 1

print(count)
