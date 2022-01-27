a = int(input())
w = a % 10
z = (a // 10) % 10
y = (a // 100) % 10
x = a // 1000
if x + w == y - z:
    print('ДА')
else:
    print('НЕТ')
    