import sys

input = sys.stdin.readline

n = int(input())

count = 0

for i in range(9):
    count += int(input())

print(n-count)
