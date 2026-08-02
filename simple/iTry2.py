a = []
n = int(input())
print()

for i in range(n):
    x = int(input())
    a.append(x)
b = sorted(a)

print()
print(b[-1])
print(b[-2])