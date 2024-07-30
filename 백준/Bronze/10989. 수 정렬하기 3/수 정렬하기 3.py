import sys
n = int(sys.stdin.readline())
ascending = [0]*10001

for i in range(n):
    number = int(sys.stdin.readline())
    ascending[number] += 1

for j in range(1,10001):
    if ascending[j] != 0:
        for k in range(ascending[j]):
            print(j)