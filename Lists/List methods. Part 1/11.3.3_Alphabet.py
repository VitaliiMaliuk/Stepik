s = []
abc = 'abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    s.append(chr(ord('a') + i)*(i+1))
print(s)
