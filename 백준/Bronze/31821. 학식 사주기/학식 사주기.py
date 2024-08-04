n = int(input())
menu = []
price = 0
for i in range(n):
    menu.append(int(input()))
    
m = int(input())

for i in range(m):
    ans = int(input())
    price += menu[ans-1]
print(price)

