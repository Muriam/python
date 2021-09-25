# rle-декодирование
def rle_decode(data): 
    decode = '' 
    count = '' 
    for char in data: 
        if char.isdigit():      # если символ числовой        
            count += char       # добавить его в счетчик
        else:                   # иначе
            decode += char * int(count) 
            count = '' 
    return decode

stroka = input('введи строку (например 2a4z): ')
decoded_val = rle_decode(stroka)

with open("test.txt", "w") as f:
    f.write(stroka)
    f.write('\n')
    f.write(decoded_val)
    print(stroka,'\n',decoded_val)