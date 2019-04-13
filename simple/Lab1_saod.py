# отсортировать список: пузырьковой, методом прямого выбора, и шейкерной сортировками. Подчситать кол-во сравнений и пересылок.
from random import randint

comparison = 0
transfer = 0
comparison2 = 0
transfer2 = 0

arr = [randint(1, 100) for _ in range(10)]
size = len(arr)

def bubble_sort():
    global comparison                                   # сравнений
    global transfer                                     # пересылок
    for i in range(9):
        for j in range(9 - i):
            comparison += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                transfer += 1

def select_sort():
    global comparison2                                  
    global transfer2
    for i in range(size - 1):
        for j in range(i + 1, size):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    comparison2 = (int(((size * size) - size) / 2));            

def shaker_sort():
    left = 0
    right = len(arr) - 1
    while left <= right:
        for i in range(left, right, +1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1                
        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
        
print('\noriginal array\n', *arr)

bubble_sort()    
print('\nbubble sort\n', *arr)
print('comparisons: ', comparison)
print('transfers: ', transfer)

select_sort()               
print('\nselection sort\n', *arr)
print('comparisons: ', comparison2)

#shaker_sort()               
#print('\nshaker sort\n', *arr) 
