from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)

# высота и ширина прямоугольника
height = 4
width = 17

# верхняя граница прямоугольника с фиолетовыми звёздочками
print(Fore.MAGENTA + '*' * width)

# боковые границы прямоугольника с фиолетовыми звёздочками
for _ in range(height - 2):                              # Высота - 2, так как верх и низ уже выведены
    print(Fore.MAGENTA + '*' + ' ' * (width - 2) + '*')  # Пробелы между звёздочками

# нижняя граница прямоугольника с фиолетовыми звёздочками
print(Fore.MAGENTA + '*' * width)


# или можно так, более лаконично, без излишеств
print("""
*****************
*               *
*               *
*****************""")