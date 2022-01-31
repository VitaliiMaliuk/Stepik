a = int(input())
x = a % 10
y = a % 100 // 10
z = a % 1000 // 100
p = max(x, y, z)
d = min(x, y, z)
g = (x + y + z) - p - d
if g == p - d:
    print('Число интересное')
else:
    print('Число неинтересное')
