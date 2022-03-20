s = list(map(int, input().split()))
n = len(s)
x = []

for i in range(n):
    if s[i] > 0:
        x.append(s[i])
if x:
    print(min(x))
else:
    print('Empty')