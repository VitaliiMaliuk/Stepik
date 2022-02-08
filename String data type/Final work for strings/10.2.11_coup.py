s = input()
s1 = s[:s.find('h') + 1]
s2 = s[s.rfind('h') - 1:s.find('h'): - 1]
s3 = s[s.rfind('h'):]
s = s1 + s2 + s3
print(s)
