# посчитайте сумму цифр введенного с клавиатуры трехзначного числа

num = int(input('введите трехзначное число '))
arr = [int(x) for x in str(num)]

if len(arr) == 3: 
    print(sum(arr))
elif len(arr) != 3:
    print('вы ввели не трехзначное число')

