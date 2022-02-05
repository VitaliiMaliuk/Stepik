n = int(input())
num = str()
while n > 0:
    num = str(n % 2) + num
    n = n // 2
print(num)
