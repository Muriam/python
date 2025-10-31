# -*- coding: utf-8 -*-

#даны четыре числа, на сколько их сумма меньше их произведения

x1=float(input("введите первое число \n"))
x2=float(input("введите второе число \n"))
x3=float(input("введите третье число \n"))
x4=float(input("введите четвертое число \n"))

sum = x1 + x2 + x3 + x4
con = x1 * x2 * x3 * x4

if sum < con:
    result = con - sum
    result = float('{:.2f}'.format(result)) #это задает 2 цифры после запятой во float
    print("результат", result)
