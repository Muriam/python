
number = list(input())

if len(number) == 4 and all(digit.isdigit() for digit in number):  # Проверка на 4 цифры и что все символы - цифры
    print(f'Цифра в позиции тысяч равна {number[0]}')
    print(f'Цифра в позиции сотен равна {number[1]}')
    print(f'Цифра в позиции десятков равна {number[2]}')
    print(f'Цифра в позиции единиц равна {number[3]}')
else:
    print('Вы ввели не четырехразрядное число')
