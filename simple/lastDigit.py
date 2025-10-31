a, b = int(input()), int(input())

count = 0

for i in range(a, b+1):
    cube = i ** 3
    last_digit = cube % 10     # последняя цифра куба
    if last_digit == 4 or last_digit == 9:
        count += 1

print(count)


