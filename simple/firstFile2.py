#import csv      - можно было и с помощью этой библиотеки


# считывание матрицы из файла
with open('in.txt') as f:
    matrix = [list(map(int, row.split())) for row in f.readlines()]
    
# сохранение матрицы в другой файл    
with open('output.txt', 'w') as f:
    for row in matrix:
        f.write(' '.join(map(str, row)) + '\n')


print('\nматрица(список списков):')
#print(*matrix)      это лишнее, гораздо красивее отображение, см цикл ниже
for i in matrix:
    for j in i:
        print(j, end=' ')
    print()

print('\nсумма элементов матрицы:')
print(sum(map(sum, matrix)))
