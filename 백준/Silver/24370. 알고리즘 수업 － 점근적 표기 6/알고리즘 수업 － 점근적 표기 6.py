a2,a1,a0 = map(int,input().split())
c1,c2 = map(int,input().split())
n0 = int(input())

def g(x):
    return c1*(x**2)
def f(x):
    return a2 * (x**2) + a1 * x + a0
def h(x):
    return c2*(x**2)

D1 = (a1**2) - 4 * a0 * (a2 - c1) #판별식 계산

D2 = (a1**2) - 4 * a0 * (a2 - c2) #판별식 계산

condition1 = False

if a2 == c1:
    if a1 == a0 == 0:
        condition1 = True
    else:
        if a1 >= 0: # 2차 함수 축이 왼쪽으로 이동 -> 오른쪽에서 교점 생기면서 f(x)가 더 커
            condition1 = True
        elif a1 == 0: # y축으로 a0만큼 대칭이동 한 것이므로 a0가 0 보다 크면 안 됨
            if a0 >= 0:
                condition1 = True
            else:
                condition1 = False
        else:# 2차 함수 축이 오른쪽으로 이동 -> 왼쪽에 교점 생겨서 상관 없음 
            condition1 = False
elif a2 == 0:
    if f(n0) >= g(n0):
        condition1 = True
    else:
        condition1 = False
elif a2 < c1:
    condition1 = False
elif D1 < 0:
    if f(n0) >= g(n0):
        condition1 = True
    else:
        condition1 = False
elif D1 == 0:
    if f(n0) >= g(n0):
        condition1 = True
    else:
        condition1 = False
else: # D > 0
    x1 = (a1 + D1**(1/2)) / (2 * (c1 - a2))
    x2 = (a1 - D1**(1/2)) / (2 * (c1 - a2))
    x = max(x1, x2)  # 두 근 중에서 큰 값을 선택
    if a2 > 0: # 아래로 볼록한 함수일 경우 
        vertex = a1 / (2 * (c1 - a2))
        if f(vertex) > g(vertex):
            condition1 = False
        else:
            if x <= n0: # 만나는 점의 x 좌표보다 n0이 클 경우는 상관 없음
                condition1 = True
            else:
                condition1 = False
    else: # 위로 볼록한 함수일 경우
        if n0 <= x: 
            condition1 = False
        else:
            condition1 = True



condition2 = False
if a2 == c2:
    if a1 == a0 == 0:
        condition2 = True
    else:
        if a1 > 0: # 2차 함수 축이 왼쪽으로 이동 -> 오른쪽에서 교점 생기면서 f(x)가 더 커
            condition2 = False
        elif a1 == 0: # y축으로 a0만큼 대칭이동 한 것이므로 a0가 0 보다 크면 안 됨
            if a0 > 0:
                condition2 = False
            else:
                condition2 = True
        else:# 2차 함수 축이 오른쪽으로 이동 -> 왼쪽에 교점 생겨서 상관 없음 
            condition2 = True
elif a2 == 0:
    if f(n0) <= h(n0):
        condition2 = True
    else:
        condition2 = False
elif a2 > c2: # (a2-c)x**2 -> 교점에서 f(x)가 더 커
    condition2 = False
elif D2 < 0 : # 만나지 않을 경우
    if f(n0) <= h(n0):
        condition2 = True
    else:
        condition2 = False
elif D2 == 0: # 한 점에서 만날 경우
    if f(n0) <= h(n0):
        condition2 = True
    else:
        condition2 = False
else: # 두 점에서 만날 경우
    x = (a1 + D2**(1/2)) / (2 * (c2 - a2)) # 근의 공식 사용해서 x값 구함 이 때 더 큰 근을 이용
    if a2 > 0: # 아래로 볼록한 함수일 경우 
        vertex = a1 / (2 * (c2 - a2))
        if f(vertex) < h(vertex):
            condition2 = False
        else:
            if x <= n0: # 만나는 점의 x 좌표보다 n0이 클 경우는 상관 없음
                condition2 = True
            else:
                condition2 = False
    else: # 위로 볼록한 함수일 경우
        if x <= n0:
            condition2 = True
        else:
            condition2 = False
            
if condition1== True and condition2 == True :
    print(1)
else:
    print(0)
