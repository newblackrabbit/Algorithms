science = []
social = []
for i in range(4):
    science.append(int(input()))
for i in range(2):
    social.append(int(input()))

science.sort()
social.sort()

science = science[1:]
social = social[1]

print(sum(science)+social)
