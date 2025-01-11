num1, num2, num3 = int(input()), int(input()), int(input())

numbers = [num1, num2, num3]
sorted_numbers = sorted(numbers, reverse=True)

for number in sorted_numbers:
    print(number)