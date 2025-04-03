# Эвклидово расстояние
import math

# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
x1, y1, x2, y2 = map(float, input().split())

result = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(result)
print(f'{result:.2f}')      # округлять можно через f-строку
print(round(result, 2))

