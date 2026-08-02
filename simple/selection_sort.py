from random import randint

array = [randint(1, 100) for _ in range(10)]

print('original array')
print(*array)

for i in range(len(array) - 1):
    for j in range(i + 1, len(array)):
        if array[j] < array[i]:
            array[i], array[j] = array[j], array[i]

print('selection sort')
print(*array)
