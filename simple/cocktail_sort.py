#https://ru.wikipedia.org/wiki/Сортировка_перемешиванием
from random import randint

array = [randint(1, 100) for _ in range(10)]
left = 0
right = len(array) - 1

print('original array')
print(*array)

print('coctail sort')
while left <= right:
    for i in range(left, right, +1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    right -= 1

    for i in range(right, left, -1):
        if array[i - 1] > array[i]:
            array[i], array[i - 1] = array[i - 1], array[i]
    left += 1

print(*array)
