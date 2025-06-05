m, n = int(input()), int(input())

if m <= n:
    for i in range(m, n+1):
        # если число: кратно 17, или оканчивается на 9, или кратно 3 и 5
        if (i % 17 == 0) or (i % 10 == 9) or (i % 3 == 0 and i % 5 == 0):
            print(i)