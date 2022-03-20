# найти минимальный положительный элемент списка (значение которого > 0)
arr = list(map(int, input().split()))
n = len(arr)
arr2 = []

for i in range(n):
    if arr[i] > 0:
        arr2.append(arr[i])
if arr2:                    # если список2 не пуст
    print('минимальный положительный элемент = ', min(arr2))
else:
    print('Empty')