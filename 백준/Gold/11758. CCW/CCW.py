#신발끈 공식

def ccw(p1,p2,p3):
    return (p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]) - (p2[0]*p1[1]+p3[0]*p2[1]+p1[0]*p3[1])

lst = []

for i in range(3):
    lst.append(list(map(int,input().split())))
    
result = ccw(lst[0],lst[1],lst[2])

if result > 0:
    print(1)
elif result == 0:
    print(0)
else:
    print(-1)
