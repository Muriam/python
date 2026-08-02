import math

x_deg = float(input())      # Ввод угла в градусах
x_rad = math.radians(x_deg) # Перевод в радианы

# Вычисление выражения sin(x) + cos(x) + tan(x)**2
result = math.sin(x_rad) + math.cos(x_rad) + math.tan(x_rad)**2

print(result)