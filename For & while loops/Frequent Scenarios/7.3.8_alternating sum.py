n = int(input())
counter = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        counter = counter + (-i)
    else:
        counter = counter + i
print(counter)
