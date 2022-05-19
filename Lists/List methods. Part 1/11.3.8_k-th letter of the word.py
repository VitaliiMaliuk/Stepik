n = int(input())
spisok = []
for i in range(n):
    s = input()
    spisok.append(s)
k = int(input())
x1 = ''
x2 = ''
for j in range(n):
    if len(spisok[j]) >= k:
        x1 = spisok[j][k - 1]
        x2 += x1
print(x2)
