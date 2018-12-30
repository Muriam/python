#чтение файла и вывод на экран

with open('text.txt', 'r+', encoding='utf_8') as file:
    data = []
    data = list(file)
    
    for row in file.readlines():
        data.append(row)
	
    print(*data)
