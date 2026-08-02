limit = int(input())

fibonacci = []
a, b = 1, 1                 # начинаю ряд с 1, 1

for _ in range(1000):       # 1000 - это максимально возможное количество итераций
    if a > limit:           # верхняя граница числа Фибоначчи - это limit (число введенное с клавиатуры)
        break
    fibonacci.append(a)
    a, b = b, a + b

print(*fibonacci)