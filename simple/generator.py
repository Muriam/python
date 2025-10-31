# n1, n2, n3, n4, n5 = float(input()), float(input()), float(input()), float(input()), float(input())
# numbers = [n1, n2, n3, n4, n5]
numbers = [float(input()) for _ in range(5)]

res = sum(abs(num) for num in numbers)              # Сумма абсолютных значений
print(res)