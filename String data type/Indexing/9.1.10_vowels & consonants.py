s = input()
countgl = 0
countsog = 0
for c in s:
    if c in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        countgl += 1
    if c in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        countsog += 1
print('Количество гласных букв равно', countgl)
print('Количество согласных букв равно', countsog)
