# ввожу слова и они выводятся, пока не напишу слово - КОНЕЦ или конец
# бесконечный цикл пока уловие - правда

words = []

while True:
    word = input()
    if word == "КОНЕЦ" or word == "конец":
        break
    words.append(word)              # добавление слова в список

print()
for w in words:                     # Вывод всех слов
    print(w)