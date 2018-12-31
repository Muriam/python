#чтение файла и вывод на экран
try:
    f = open('text.txt', 'a')
    while(True):
        f.write(input())
        f.write('\n')
except KeyboardInterrupt:
    f.write('\n')
    f.close()
