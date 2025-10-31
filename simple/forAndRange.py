# вывод нечетных чисел по убыванию, при m > n
m, n = int(input()), int(input())

if m > n:
    for i in range(m, n-1, -1):
        if i % 2 != 0:
            print(i)