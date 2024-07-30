import sys

n = int(sys.stdin.readline())
number = []

for i in range(n):
    num = int(sys.stdin.readline())
    number.append(num)

number.sort()

for i in range(n):
    print(number[i])
