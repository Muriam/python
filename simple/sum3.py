
# На вход программе подаётся натуральное число n
# Программа подсчитывает сумму тех чисел от 1 до n (включительно), 
# квадрат которых оканчивается на 2, 5 или 8

n = int(input())

total = 0

for i in range(1, n + 1):
    square = i ** 2
    last_digit = square % 10
    if last_digit in {2, 5, 8}:
        total += i

print(total)