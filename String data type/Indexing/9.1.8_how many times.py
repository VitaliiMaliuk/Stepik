s = input()
count = 0
count1 = 0
for i in range(len(s)):
    if s[i] == '+' in s:
        count += 1
    if s[i] == '*' in s:
        count1 += 1
print('Символ + встречается', count, 'раз')
print('Символ * встречается', count1, 'раз')
