numbers = []

count = 0

while count < 5:
    try:
        num = int(input('введите целое число '))
        numbers.append(num)
        count += 1
    except ValueError:
        print('введите корректное целое число')


print("список:", *numbers)
minimum = min(numbers)
maximum = max(numbers)

print(f'наименьшее число = {minimum}')
print(f'наибольшее число = {maximum}')