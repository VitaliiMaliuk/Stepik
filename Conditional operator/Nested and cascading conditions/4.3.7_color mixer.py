x = str(input())
y = str(input())
z = 'желтый'
if x == 'красный' and y == 'синий' or x == 'синий' and y == 'красный':
    print('фиолетовый')
elif x == 'красный' and y == 'желтый' or x == 'желтый' and y == 'красный':
    print('оранжевый')
elif x == 'синий' and y == 'желтый' or x == 'желтый' and y == 'синий':
    print('зеленый')
elif x == y == 'красный':
    print('красный')
elif x == y == 'синий':
    print('синий')
elif x == y == 'желтый':
    print('желтый')
else:
    print('ошибка цвета')