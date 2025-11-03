n = int(input())            # введите одно число
result = 0

for i in range(1, n + 1):
    if i % 2 == 1:          # нечётные числа складываются
        result += i
    else:                   # чётные числа вычитаются
        result -= i

print(result)
    