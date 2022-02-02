n = int(input())
while n != 0:
    lastnum = n % 10
    n = n // 10
    print(lastnum, end='')
