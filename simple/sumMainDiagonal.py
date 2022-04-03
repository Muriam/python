n = int(input())    # cписок размером NxN
sum = 0             
arr = []
arr2 = []

for i in range(n):
    for j in range(i):
        arr2.append(j)
    arr.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(n):
        if i == j:
            sum += arr[i][j]
            
print(sum)          # sum - это сумма элементов главной диагонали