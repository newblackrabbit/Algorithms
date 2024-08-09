a = list(input())  
b = input().split()

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            a[i] = a[i].lower()
            continue
        

for i in a:
    print(i, end='')
