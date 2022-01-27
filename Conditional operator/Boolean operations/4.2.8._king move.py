a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a - 1 == c and b + 1 == d) or (a - 1 == c and b == d) or (a - 1 == c and b - 1 == d) or (a == c and b + 1 == d) or (a == c and b == d) or (a == c and b - 1 == d) or (a + 1 == c and b + 1 == d) or (a + 1 == c and b == d) or (a + 1 == c and b - 1 == d):
    print('YES')
else:
    print('NO')
