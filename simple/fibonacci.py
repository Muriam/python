fibonacci = []
a, b = 1, 1             # начинаю ряд с 1, 1

for _ in range(20):     # максимально возможное количество чисел Фибоначчи до 100
    if a > 100:
        break
    fibonacci.append(a)
    a, b = b, a + b

print(*fibonacci)