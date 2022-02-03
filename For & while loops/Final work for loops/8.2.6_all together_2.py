n = int(input())
kolvotri = 0
kolvopol = 0
bolp = 0
countp = 0
proizvsem = 1
kolnp = 0
x = n % 10
while n != 0:
    ld = n % 10
    if ld == 3:
        kolvotri += 1
    if  x == ld:
        countp += 1
    if ld % 2 == 0:
        kolvopol += 1
    if ld > 5:
        bolp += ld
    if ld > 7:
        proizvsem *= ld
    if ld == 0 or ld == 5:
        kolnp += 1
    n = n // 10
print(kolvotri, countp, kolvopol, bolp, proizvsem, kolnp, sep='\n')
