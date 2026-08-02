n = int(input())

summa_delitelei = 0

for i in range(1, n + 1):
    # проверка, является ли i делителем n
    if n % i == 0:
        summa_delitelei += i

print(summa_delitelei)