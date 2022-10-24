p1 = [int(x) for x in input().split()]
p2 = [int(x) for x in input().split()]
p3 = [int(x) for x in input().split()]
p4 = [int(x) for x in input().split()]
p5 = [int(x) for x in input().split()]
all = [p1, p2, p3, p4, p5]
sol = []
for i in all:
    sol.append(sum(i))
print(sol.index(max(sol))+1, max(sol))
