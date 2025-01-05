'''
если число нечётное, то вывести «YES»;
если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
если число чётное и больше 20, то вывести «NO».
'''

number = int(input())

if number % 2 != 0:
    print('YES')
elif number in range(2, 6, 2):
    print('NO')
elif number in range(6, 21, 2):
    print('YES')
elif number > 20 and number % 2 == 0:
    print('NO')