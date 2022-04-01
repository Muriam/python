arr = list(map(int, input().split()))             # введите элементы массива(списка)
n = len(arr) 

for j in range(n):
    key = arr[j]
    i = j - 1
    while i >= 0 and arr[i] > key:
        arr[i+1] = arr[i]
        i -= 1
    arr[i+1] = key
 
print(*arr)                                      # список, отсортированный вставками



'''
аглоритм сортировки вставками взят из следущего псевдокада: 

for j = 2 to A.length do 
    key = A[j]
    i = j-1
    while (int i > 0 and A[i] > key) do 
        A[i + 1] = A[i]
        i = i - 1
    end while
    A[i+1] = key
end
'''