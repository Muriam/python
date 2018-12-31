from random import randint

arr = [randint(1, 100) for _ in range(10)]

def bubble_sort():
    for i in range(9):
        for j in range(9 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def select_sort():
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

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
        
print('original array\n', *arr)
#bubble_sort()    
#print('bubble sort\n', *arr)
#select_sort()               
#print('selection sort\n', *arr)
shaker_sort()               
print('shaker sort\n', *arr) 