lst = []

for _ in range(10):
    i = int(input())    
    if i % 2 == 0:        
        lst.append(i)   

print('\n', *lst, '\n')

if len(lst) == 10:
    print('YES')
else:
    print('NO')    