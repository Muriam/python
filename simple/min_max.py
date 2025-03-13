city1, city2, city3 = input(), input(), input()
length1, length2, length3 = len(city1), len(city2), len(city3)

small = min(length1, length2, length3)
big = max(length1, length2, length3)

print()

# самое короткое название города
if small == length1:
    print(city1)
elif small == length2:
    print(city2)
else:
    print(city3)

# самое длинное название города
if big == length1:
    print(city1)
elif big == length2:
    print(city2)
else:
    print(city3)