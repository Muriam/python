n = int(input())
print()

# инициализация первыми двумя числами
max1 = int(input())
max2 = int(input())

# убедюсь, что max1 >= max2
if max2 > max1:
    max1, max2 = max2, max1

# обработка остальных n-2 чисел
for _ in range(n - 2):
    num = int(input())
    
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

print()
print(max1)
print(max2)