from random import random


lis = [0] * 10
for i in range(10):
    lis[i] = int(random() * 100)
print('original list', lis)

for i in range(9):
    for j in range(9 - i):
        if lis[j] > lis[j + 1]:
            lis[j], lis[j + 1] = lis[j + 1], lis[j]
print('bubble sort', lis)
