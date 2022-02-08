s = input()
count = 0
max = 0
for c in s:
    if s.count(c) >= count:
        count = s.count(c)
        max = c
print(max)
