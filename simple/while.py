#Вывести число, если оно в диапазоне от 10 до 100
while True:
    try:
        x = int(input())
    except:
        pass
    if x >= 10 and x <= 100:
        print(x)
    elif x < 10:
        continue
    elif x > 100:
        break
