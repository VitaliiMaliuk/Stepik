a = int(input())
b = int(input())
c = int(input())
if a == b != c or a != b == c or a == c != b:
    print('Равнобедренный')
elif a == b == c:
    print('Равносторонний')
else:
    print('Разносторонний')
