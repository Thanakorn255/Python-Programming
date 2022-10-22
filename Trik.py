inp = input()
box1 = []
box2 = []
box3 = []
ball = 1
box1.append(ball)
for i in inp:
    if i == 'A':
        if ball in box2:
            box1.append(ball)
            box2.clear()
        else:
            box2.append(ball)
            box1.clear()
    elif i == 'B':
        if ball in box3:
            box2.append(ball)
            box3.clear()
        else:
            box3.append(ball)
            box2.clear()
    elif i == 'C':
        if ball in box1:
            box3.append(ball)
            box1.clear()
        else:
            box1.append(ball)
            box3.clear()
if ball in box1:
    print('1')
elif ball in box2:
    print('2')
elif ball in box3:
    print('3')
