n = int(input())
s = input()
for i in s:
    sumb = ord(i) - n
    if sumb < 97:
        sumb = 122 - (96 - sumb)
    print(chr(sumb), end='')
