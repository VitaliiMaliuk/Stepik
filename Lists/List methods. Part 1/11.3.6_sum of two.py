n = int(input())
s = []
count = 0
for i in range(n):
    num = int(input())
    count += num
    s.append(count)
    count = num
print(s[1:])
