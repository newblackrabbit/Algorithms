n = int(input())
d = 0
p = 0
for i in range(n):
    if d-p == 2 or p-d == 2:
        break
    ans = input()
    if ans == 'D':
        d += 1
    else:
        p += 1

print(str(d)+':'+str(p))
