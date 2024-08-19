a2,a1,a0 = map(int,input().split())
c = int(input())
n0 = int(input())

def g(x):
    return c*(x**2)
def f(x):
    return a2 * (x**2) + a1 * x + a0

D = (a1**2) - 4 * a0 * (a2 - c) #판별식 계산

if a2 == c:
    if a1 == a0 == 0:
        print(1)
    else:
        if a1 > 0: # 2차 함수 축이 왼쪽으로 이동 -> 오른쪽에서 교점 생기면서 f(x)가 더 커
            print(0)
        elif a1 == 0: # y축으로 a0만큼 대칭이동 한 것이므로 a0가 0 보다 크면 안 됨
            if a0 > 0:
                print(0)
            else:
                print(1)
        else:# 2차 함수 축이 오른쪽으로 이동 -> 왼쪽에 교점 생겨서 상관 없음 
            print(1)
elif a2 == 0:
    if f(n0) <= g(n0):
        print(1)
    else:
        print(0)
elif a2 > c: # (a2-c)x**2 이 위로 볼록 함수 됨 -> 0보다 큼
    print(0)
elif D < 0 : # 만나지 않을 경우
    if f(n0) <= g(n0):
        print(1)
    else:
        print(0)
elif D == 0: # 한 점에서 만날 경우
    if f(n0) <= g(n0):
        print(1)
    else:
        print(0)
else: # 두 점에서 만날 경우
    x = (a1 + D**(1/2)) / (2 * (c - a2)) # 근의 공식 사용해서 x값 구함 이 때 더 큰 근을 이용
    if a2 > 0: # 아래로 볼록한 함수일 경우 
        vertex = a1 / (2 * (c - a2))
        if f(vertex) < g(vertex):
            print(0)
        else:
            if x <= n0: # 만나는 점의 x 좌표보다 n0이 클 경우는 상관 없음
                print(1)
            else:
                print(0)
    else: # 위로 볼록한 함수일 경우
        if x <= n0:
            print(1)
        else:
            print(0)