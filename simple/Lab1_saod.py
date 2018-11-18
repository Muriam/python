from random import randint

def random_array(list):
    list = [randint(1, 100) for _ in range(10)]
    return list

arr = random_array(list)    
print('original list\n', *arr)
