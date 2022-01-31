a = len(input())
b = len(input())
c = len(input())
d =a + b + c - min(a, b, c) - max(a, b, c)
if max(a, b, c) - d == d - min(a, b, c):
    print('YES')
else:
    print('NO')
