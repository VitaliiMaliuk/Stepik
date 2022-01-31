from math import sqrt
a = float(input())
b = float(input())
Sa = (a + b) / 2
Sg = sqrt(a * b)
Sgar = (2 * a * b) / (a + b)
Sq = sqrt((a ** 2 + b ** 2) / 2)
print(Sa, Sg, Sgar, Sq, sep='\n')
