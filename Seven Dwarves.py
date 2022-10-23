c = 9
num = []
sol = []
while c >= 1:
    inp = int(input())
    num.append(inp)
    c -= 1
sum = sum(num)
num100 = sum-100
for i in num:
    for j in range(len(num)):
        if i+num[j] == num100 and i != num[j]:
            sol.append(i)
for k in sol:
    num.remove(k)
for p in num:
    print(p)
