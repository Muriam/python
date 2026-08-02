import math

a, b, c = float(input()), float(input()), float(input())

D = b**2 - 4 * a * c             # дискриминант            

if D < 0:
    print('Нет корней')
elif D == 0:
    x = -b / (2 * a)             
    print(f'корень уравнения: \n {x}')                
else:
    sqrt_D = math.sqrt(D)        # квадратный корень из дискриминанта
    x1 = (-b - sqrt_D) / (2 * a)
    x2 = (-b + sqrt_D) / (2 * a)
    roots = sorted([x1, x2])     # сортирую по возрастанию
    print('корни уравнения:')
    print(roots[0], roots[1], sep='\n')
   