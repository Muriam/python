def insertion_sort(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i = i - 1
            else:
                break
            
array = [9, 23, 678, 8, -88, -2, 3, 8, 45, 111]
print('original list ', array)
insertion_sort(array)
print('insertion sort', array)
