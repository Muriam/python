permutations = 0        

n = int(input())                            # n - это количество элементов в массиве
arr = list(map(int, input().split()))       # введите элементы массива(списка)

for i in range(n-1):
    for j in range((n-1) - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            permutations += 1
            
print(*arr)             # отсортированый пузырьком массив
print(permutations)     # количество перестановок