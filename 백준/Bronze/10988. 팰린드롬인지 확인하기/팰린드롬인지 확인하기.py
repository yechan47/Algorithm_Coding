a = input()

if a[::1] == a[::-1]:
    print(1)
else:
    print(0)