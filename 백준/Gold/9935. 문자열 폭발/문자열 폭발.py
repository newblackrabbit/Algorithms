import sys
input = sys.stdin.readline

n = list(input().strip())
m = list(input().strip())

stack = []

for i in n:
    stack.append(i)
    if stack[len(stack)-len(m):len(stack)] == m:
        for j in range(len(m)):
            stack.pop()

if stack:
    for i in stack:
        print(i,end='')
else:
    print('FRULA')
