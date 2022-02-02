x = int(input())
total = 0
while x > 0:
    n = x
    if 1 <= x < 5:
        total += 1
        x = x - 1
    elif 5 <= x < 10:
        total += 1
        x = x - 5
    elif 10 <= x < 25:
        total += 1
        x = x - 10
    elif x >= 25:
        total += 1
        x = x - 25
print(total)
