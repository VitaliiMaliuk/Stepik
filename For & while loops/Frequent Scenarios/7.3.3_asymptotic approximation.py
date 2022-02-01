import math
n = int(input())
num = 0
for i in range(n):
    num = num + 1 / (i + 1)
    num1 = num - math.log(n)
print(num1)
