x = int(input())
if ((1 <= x <= 10 or 19 <= x <= 28) and x % 2 != 0) or ((11 <= x <= 18 or 29 <= x <= 36) and x % 2 == 0):
    print('красный')
elif x == 0:
    print('зеленый')
elif 0 > x or x > 36:
    print('ошибка ввода')
else:
    print('черный')
    