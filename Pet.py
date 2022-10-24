p1 = [int(x) for x in input().split()]
p2 = [int(x) for x in input().split()]
p3 = [int(x) for x in input().split()]
p4 = [int(x) for x in input().split()]
p5 = [int(x) for x in input().split()]
all = [p1, p2, p3, p4, p5]
sol = []
max_sol = 0
for i in all:
    sol.append([sum(i)])
max_in = sol.index(max(sol))+1
sol.sort()
for j in sol[-1]:
    max_sol += int(j)
print(max_in, max_sol)
