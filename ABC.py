num = [int(x) for x in input().split()]
d_set = input()
cha = []
ans = []
num.sort()
for i in d_set.upper():
    cha.append(i)
for j in cha:
    if j == 'A':
        ans.append(str(num[0]))
    elif j == 'B':
        ans.append(str(num[1]))
    else:
        ans.append(str(num[2]))
ans = " ".join(ans)
print(ans)
