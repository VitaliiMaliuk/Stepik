n = int(input())
largest = 1
prelargest = 0
for i in range(1, n + 1):
    num = int(input())
    if num > largest:
        prelargest = largest
        largest = num
    elif num < largest and num > prelargest:
        prelargest = num
print(largest, prelargest, sep='\n')
