n = int(input())
total = 0
for i in range(n):
    for j in range(i + 1):
        print(total + 1, end=' ')
        total += 1
    print()
