# вывод "ДА" - если это арифметическая прогрессия (одинаковые интервалы между цифрами, то есть длинами введенных строк):

# вариант решения более элегантный
a, b, c = sorted(len(input()) for _ in range(3))

match (b - a == c - b):
    case True:
        print('YES')
    case _:
        print('NO')

print()


# вариант решения другой, к этой же задаче
lengths = {
    'first': len(input()),
    'second': len(input()),
    'third': len(input())
}

sorted_lengths = sorted(lengths.values())   # Извлечение значений и сортировка

if sorted_lengths[1] - sorted_lengths[0] == sorted_lengths[2] - sorted_lengths[1]:
    print('YES')
else:
    print('NO')
