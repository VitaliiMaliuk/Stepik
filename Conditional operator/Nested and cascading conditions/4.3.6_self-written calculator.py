x = int(input())
y = int(input())
z = str(input())
if z == '+':
    print(x + y)
elif z == '-':
    print(x - y)
elif z == '*':
    print(x * y)
elif z == '/':
    if y == 0:
        print('На ноль делить нельзя!')
    else:
        print(x / y)
else:
    print('Неверная операция')
    