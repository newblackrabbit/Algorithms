word = []
for i in range(3):
    n = input()
    word.append(n)
    
l = k  = p = False

for i in word:
    if i[0] == 'l':
        l = True
    if i[0] == 'k':
        k = True
    if i[0] == 'p':
        p = True

if k == l == p == True:
    print('GLOBAL')
else:
    print('PONIX')
