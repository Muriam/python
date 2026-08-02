# отсортировать список: пузырьковой, методом прямого выбора, и шейкерной сортировками. Подчситать кол-во сравнений и пересылок.
from random import randint

arr = [randint(1, 100) for _ in range(10)]
arr2 = arr.copy()        # создание копии списка, чтоб selection_sort происходила повторно с такими же числами, как было у bubble_sort
size = len(arr)

def bubble_sort(comparison=0, transfer=0):
    for i in range(9):
        for j in range(9 - i):
            comparison += 1                         # подсчет сравнений
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                transfer += 1                       # подсчет пересылок
    return comparison, transfer
        
def select_sort(comparison2=0, transfer2=0):
    for i in range(size-1):
        min = i
        for j in range(i+1, size):
            if (arr2[j] < arr2[min]):
                min = j
        if (min == i): 
            continue
        temp = arr2[i]
        arr2[i] = arr2[min]
        arr2[min] = temp
        transfer2 += 1                                 
    comparison2 = (int(((size * size) - size) / 2))
    return comparison2, transfer2          

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

comparison, transfer = bubble_sort()    
print('\nbubble sort\n', *arr)
print('comparisons: ', comparison)
print('transfers: ', transfer)

comparison2, transfer2 = select_sort()               
print('\nselection sort\n', *arr)
print('comparisons: ', comparison2)
print('transfers: ', transfer2)

#shaker_sort()               
#print('\nshaker sort\n', *arr) 
