#вывод файла на экран
f = open ('text.txt', 'rw')
print (f.read())

'''
for line in f:      то же самое другим способом
	print(line)

f.write ('...')     записать что-то в файл, отображается в блокноте
f.close()     
'''
