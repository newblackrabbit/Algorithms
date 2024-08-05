x,y = input().split()

def rev(x):
    return x[::-1]

x = rev(x)
y = rev(y)

print(int(rev(str(int(x)+int(y)))))
