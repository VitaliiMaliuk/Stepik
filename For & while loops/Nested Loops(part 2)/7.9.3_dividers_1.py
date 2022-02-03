a = int(input())
b = int(input())
summ_del = 0
max_ch = 0
for i in range(a, b + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += j
        if count >= summ_del:
            summ_del = count
            max_ch = j
print(max_ch, summ_del)
