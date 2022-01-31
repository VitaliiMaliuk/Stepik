from math import sqrt
a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if D > 0 and a != 0:
    x = (- b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    y = (- b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(min(x, y), max(x, y), sep='\n')
elif D == 0:
    x = - (b / (2 * a))
    print(x)
elif D < 0:
    print('Нет корней')
