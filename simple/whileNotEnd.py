# ввожу слова и они выводятся, пока не напишу слово - КОНЕЦ

words = []

while True:
    word = input()
    if word == "КОНЕЦ":
        break
    words.append(word)

for w in words:
    print(w)