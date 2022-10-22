from cmath import sqrt
import math
num1, num2 = [float(x) for x in input().split()]
sum = math.sqrt(num1**2+num2**2)
print(f'{sum: .6f}')
