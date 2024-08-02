mbti = input()

n = int(input())
count = 0

for i in range(n):
    ans = input()
    if mbti == ans:
        count += 1

print(count)
