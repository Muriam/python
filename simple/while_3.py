# вводится список имен. Александр должен встретиться раньше Леона.
# в этом случае вывести кол-во людей между ними

names = []

while True:
    try:
        line = input()
        names.append(line)
        if line == 'Леон': 	# Можно остановиться сразу, как встретился Левон
            break
    except EOFError: 		# Если ввод закончился раньше
        break

idx_alex = names.index('Александр')
idx_leon = names.index('Леон')

print(idx_leon - idx_alex - 1)
