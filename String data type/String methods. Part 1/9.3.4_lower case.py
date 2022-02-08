s = input()
count = 0
for i in range(len(s)):
    if "a" <= s[i] <= "z":
        count += 1
print(count)
