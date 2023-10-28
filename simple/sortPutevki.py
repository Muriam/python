lst = []

while True:
    item = input('Введите 6-значное число: ')
    lst.append(int(item)) 
    if len(item) != 6:
        break

lst.pop()
lst.sort()
print(lst)


