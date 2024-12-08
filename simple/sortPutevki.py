lst = []

while True:
    item = input('Введите 6-значное число: ')
    if len(item) != 6:
        break
    lst.append(int(item))

lst.sort()

prev = None
for num in lst:
    nums = str(num)[:3] 
    if nums != prev:
        print()  
        prev = nums
    print(num, end='\n')



