import sys
input = sys.stdin.readline

n = int(input())
people = list(map(int,input().split()))

people.sort()

time = 0
result = 0

for i in range(n):
    time += people[i]
    result += time

print(result)
