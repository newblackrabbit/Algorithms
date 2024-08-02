count = 0
while True:
    n0 = int(input())
    count += 1
    if n0 == 0:
        break
    n1 = 3*n0
    if n1 % 2 == 0:
        n2 = n1//2
    else:
        n2 = (n1+1)//2
    n3 = 3*n2
    n4 = n3//9
    if n1 % 2 == 0:
        print(str(count)+'.'+' even '+str(n4))
    else:
        print(str(count)+'.'+' odd '+str(n4))
