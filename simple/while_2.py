count = 0
stop_words = {'стоп', 'хватит', 'достаточно'}
stop_word = ' '              

while True:
    word = input()
    if word in stop_words:
        stop_word = word 
        break
    count += 1

print(f'Количество введенных слов: {count}')
print(f'Стоп-слово: "{stop_word}"')
print(f'Длина стоп-слова: {len(stop_word)} символов')