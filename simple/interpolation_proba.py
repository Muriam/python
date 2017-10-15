import math

N = 5
c = N + 1;
H = 0.011
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29] 


i = 0 
for elements in list: 
    ost = (list[i] % 4) + 1  
    x = round(c + (i * H) + (ost / 5) * H, 4)    
    print ('x =',x)
    i = i + 1  