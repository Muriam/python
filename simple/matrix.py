#вложенный список
arr = [[9, 5, 3],
       [0, 7, -1], 
       [-5, 2, 9]]

arr2 = []

#вывод списка в виде матрицы
for i in arr:
       for j in i:
              print(j, end=' ')
       print()


zn1 = arr[2][0] + arr[1][0] + arr[0][2] + arr[0][1]
zn2 = arr[2][1] + arr[1][1] + arr[0][0] + arr[0][2]
zn3 = arr[2][2] + arr[1][2] + arr[0][1] + arr[0][0]
zn4 = arr[0][0] + arr[2][0] + arr[1][2] + arr[1][1]
zn5 = arr[0][1] + arr[2][1] + arr[1][0] + arr[1][2]
zn6 = arr[0][2] + arr[2][2] + arr[1][1] + arr[1][0]
zn7 = arr[1][0] + arr[0][0] + arr[2][2] + arr[2][1]
zn8 = arr[1][1] + arr[0][1] + arr[2][0] + arr[2][2]
zn9 = arr[1][2] + arr[0][2] + arr[2][1] + arr[2][0]

print('\n', zn1, zn2, zn3, zn4, zn5, zn6, zn7, zn8, zn9)

arr2.extend([zn1, zn2, zn3, zn4, zn5, zn6, zn7, zn8, zn9])
print('\n', arr2)