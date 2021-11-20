import random

arr = [1, 2, 3, 4, 5]

yourNumber = int(input('введите число от 1 до 5: '))
computerNumber = random.choice(arr)
print(f'Вы выбрали {yourNumber}, компьютер выбрал {computerNumber}')

if yourNumber == computerNumber:
    print('вы угадали')
elif yourNumber != computerNumber:
    print('НЕ УГАДАЛИ, компьютер загадал другое число')