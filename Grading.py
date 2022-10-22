num1 = int(input())
num2 = int(input())
num3 = int(input())
sum = num1+num2+num3
if sum >= 80:
    print('A')
elif sum >= 75:
    print('B+')
elif sum >= 70:
    print('B')
elif sum >= 65:
    print('C+')
elif sum >= 60:
    print('C')
elif sum >= 55:
    print('D+')
elif sum >= 50:
    print('D')
elif sum >= 0:
    print('F')
