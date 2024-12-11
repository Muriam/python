num = list(map(int, input('введите 4-значное число ')))

if len(num) == 4 and num[0] + num[3] == num[1] - num[2]:
    print('ДА')
else:
    print('НЕТ')
