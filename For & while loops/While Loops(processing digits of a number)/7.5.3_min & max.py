n = int(input())
minimum = 9
maximum = 0
while n != 0:
    if n % 10 < minimum:
        minimum = n % 10
    if n % 10 > maximum:
        maximum = n % 10
    n = n // 10
print('Максимальная цифра равна', maximum)
print('Минимальная цифра равна', minimum)
