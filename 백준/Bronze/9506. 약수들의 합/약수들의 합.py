while True:
    n = int(input())
    if n == -1:
        break
    count = []
    for i in range(1, n):
        if n % i == 0:
            count.append(i)
    if n == sum(count):
        print(n,'=',end=' ')
        print(*count,sep=' + ')
    else:
        print(n,'is NOT perfect.')
