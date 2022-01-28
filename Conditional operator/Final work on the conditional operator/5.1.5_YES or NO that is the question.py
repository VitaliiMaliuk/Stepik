x = int(input())
if x % 2 != 0:
    print('YES')
elif 6 <= x <= 20 and x % 2 == 0:
    print('YES')
elif (2 <= x <= 5 or x > 20) and x % 2 == 0:
    print('NO')
