a = []

for i in range(9):
    a+=list(map(int, input().split()))

b = a.index(max(a))

print(max(a))
print(b//9+1, b%9+1)