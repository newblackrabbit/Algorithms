import sys
input = sys.stdin.readline

ans = []
for i in range(8):
    score = int(input())
    ans.append(score)

grade = sorted(ans)

grade.sort(reverse=True)

grade = grade[:5]

print(sum(grade))

num = []

for i in grade:
    num.append(ans.index(i))

num.sort()

for i in num:
    print(i+1,end=' ')

