n = int(input())
has_one = True
ls = n % 10
while n != 0:
    num = n % 10
    if num != ls:
       has_one = False
    n = n // 10
if has_one == True:
    print('YES')
else:
    print('NO')
    