s = input()
count = 0
for i in range(0, len(s)):
    if s[i] == 'f':
        count += 1
if count == 1:
    print('-1')
elif count == 0:
    print('-2')
else:
    s = s.replace('f', 'a', 1)
    print(s.find('f'))
    