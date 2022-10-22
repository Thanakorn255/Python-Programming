count = 10
num = []
ans = []
all = []
while count >= 1:
    inp = int(input())
    num.append(inp)
    count -= 1
for i in num:
    ans.append((i % 42))
for j in ans:
    if j not in all:
        all.append(j)
print(len(all))
