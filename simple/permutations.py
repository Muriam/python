import itertools

number = input()

# Проверка, что число трехзначное и все цифры различны
if len(number) == 3 and len(set(number)) == 3 and number.isdigit():
    permutations = itertools.permutations(number)   # Генерация всех возможных перестановок
    # Вывод всех перестановок
    for perm in permutations:
        print(''.join(perm))                        # Объединяю кортеж в строку и вывожу
else:
    print('не три числа, или они не различны')