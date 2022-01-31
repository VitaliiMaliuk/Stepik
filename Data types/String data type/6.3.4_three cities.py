a = input()
b = input()
c = input()
if  len(c) < len(b) < len(a):
    print(c, a, sep='\n')
elif len(c) < len(a) < len(b):
    print(c, b, sep='\n')
elif len(a) < len(b) < len(c):
    print(a, c, sep='\n')
elif len(b) < len(a) < len(c):
    print(b, c, sep='\n')
elif len(a) < len(c) < len(b):
    print(a, b, sep='\n')
elif len(b) < len(c) < len(a):
    print(b, a, sep='\n')
